from django.test import TestCase
from django.contrib.auth.models import User
from .models import Film, Hall, Screening, Reservation, Seat
from django.urls import reverse
from django.utils import timezone

# Create your tests here.

class ReservationTests(TestCase):
    def setUp(self):
        self.password = 'tester123'

        self.user = User.objects.create_user(
            username='tester',
            password=self.password,
            email= 'test@test.com',
        )
        self.client.login(
            username = self.user.username,
            password = self.password,
        )

        self.film = Film.objects.create(
            title = 'Matrix',
            description = 'Film about future',
            duration = 150,
            release_year = 2001,
        )

        self.hall = Hall.objects.create(
            name = 'hall_test',
            capacity = 50,
        )

        self.screening = Screening.objects.create(
            film = self.film,
            hall = self.hall,
            screening_time = timezone.now(),
        )

    def test_create_reservation_with_valid_ticket_count(self):
        response = self.client.post(
            reverse('create_reservation_url', args=[self.screening.id]), {'tickets_count': 2}
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(),1)

        reservation = Reservation.objects.first()

        self.assertEqual(reservation.user, self.user)
        self.assertEqual(reservation.screening, self.screening)
        self.assertEqual(reservation.tickets_count,2)

    def test_ticket_invalid(self):
        response = self.client.post(
            reverse('create_reservation_url', args=[self.screening.id]), {'tickets_count': 0}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(),0)
        self.assertRedirects(response, reverse('movie_detail', args=[self.screening.film.slug]))

    def test_capacity_of_halls(self):
        self.hall.capacity = 2
        self.hall.save()
        response = self.client.post(
                reverse('create_reservation_url', args=[self.screening.id]), {'tickets_count': 4})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(),0)
        self.assertRedirects(response, reverse('movie_detail', args=[self.screening.film.slug]))

    def test_update_tickets(self):
        response = self.client.post(
            reverse('create_reservation_url', args=[self.screening.id]), {'tickets_count': 2})
        reservation = Reservation.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(),1)
        self.assertEqual(reservation.tickets_count,2)
        self.assertRedirects(response, reverse('reservation'))
        
        response = self.client.post(
            reverse('create_reservation_url', args=[self.screening.id]), {'tickets_count': 4})
        reservation = Reservation.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(),1)
        self.assertRedirects(response, reverse('reservation'))
        self.assertEqual(reservation.tickets_count,4)


    def test_delete_reservation(self):
        reservation = Reservation.objects.create(
            user = self.user,
            screening = self.screening,
            tickets_count = 1
        )
        response = self.client.post(
            reverse('delete_reservation_url', args=[reservation.id]))
        self.assertRedirects(response, reverse('reservation'))
        self.assertEqual(Reservation.objects.count(),0)
    
    def test_anonymous_user_cannot_create_reservation(self):
        self.client.logout()
        response = self.client.post(
            reverse('create_reservation_url', args=[self.screening.id]), {'tickets_count': 1})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login_url') + '?next=' + reverse('create_reservation_url', args=[self.screening.id]))
        self.assertEqual(Reservation.objects.count(),0)

        
    def test_generating_seats(self):
        hall = Hall.objects.create(
            name = 'Test Hall',
            capacity = 12,
        )
        generated_seats = Seat.objects.filter(hall=hall).count()
        self.assertEqual(generated_seats,12)
        expected_seats = [
            'Test Hall - A1', 'Test Hall - A2', 'Test Hall - A3', 'Test Hall - A4', 'Test Hall - A5', 'Test Hall - A6', 'Test Hall - A7', 'Test Hall - A8', 'Test Hall - A9', 'Test Hall - A10',
            'Test Hall - B1', 'Test Hall - B2'
        ]
        
        #actual_seats = [str(seat) for seat in Seat.objects.filter(hall=hall)]
        actual_seats = []
        for seat in Seat.objects.filter(hall=hall):
            actual_seats.append(str(seat))
        self.assertListEqual(actual_seats, expected_seats)


