from django.shortcuts import render
from datetime import date

movies = [
    {
        'image': 'avengers.jpg',
        'author': 'Marvel Studios',
        'data': date(2012, 5, 4),
        'title': 'The Avengers',
        'excerpt': 'Earth\'s mightiest heroes must come together to stop the villain Loki and his alien army from enslaving humanity.',
        'content': 'Nick Fury of S.H.I.E.L.D. brings together a team of superheroes to save the Earth from the trickster god Loki and his army of Chitauri. The Avengers—Iron Man, Thor, Captain America, the Hulk, Black Widow, and Hawkeye—unite to defend the planet in a spectacular battle.'
    },
    # A Bug's Life
    {
        'image': 'bugs-life.jpeg',
        'author': 'Pixar Animation Studios',
        'data': date(1998, 11, 25),
        'title': 'A Bug\'s Life',
        'excerpt': 'A misfit ant, looking for warriors to save his colony, recruits a group of circus bugs instead.',
        'content': 'Flik, an inventive ant, teams up with a ragtag group of circus insects to defend his colony from the greedy grasshoppers led by Hopper. Together, they learn that even the smallest of heroes can make a big difference.'
    },
    # Coco
    {
        'image': 'coco.jpeg',
        'author': 'Pixar Animation Studios',
        'data': date(2017, 11, 22),
        'title': 'Coco',
        'excerpt': 'A young boy with a passion for music embarks on a magical journey to the Land of the Dead to discover his family\'s past.',
        'content': 'Miguel, a young aspiring musician, accidentally travels to the Land of the Dead, where he learns about his ancestors and uncovers the truth about his family\'s history. Along the way, he forms new bonds and reignites his passion for music.'
    },
    # The Flash
    {
        'image': 'flash.jpeg',
        'author': 'Warner Bros.',
        'data': date(2023, 6, 16),
        'title': 'The Flash',
        'excerpt': 'Barry Allen uses his super-speed to alter the past but ends up creating unintended consequences in the present.',
        'content': 'When Barry Allen (The Flash) travels back in time to prevent his mother\'s murder, he inadvertently alters the timeline, creating a new reality with dire consequences. Barry must now navigate this altered world and restore the balance of the multiverse.'
    },
    # The Incredibles
    {
        'image': 'the-incredibles.jpeg',
        'author': 'Pixar Animation Studios',
        'data': date(2004, 11, 5),
        'title': 'The Incredibles',
        'excerpt': 'A family of superheroes must come together to defeat a villain threatening the city.',
        'content': 'The Parr family, also known as The Incredibles, faces the challenges of balancing their everyday lives while using their superpowers to fight crime. Together, they must stop Syndrome, a villain who seeks to eliminate all superheroes and rule the world.'
    },
    # Thor
    {
        'image': 'thor.jpeg',
        'author': 'Marvel Studios',
        'data': date(2011, 5, 6),
        'title': 'Thor',
        'excerpt': 'The mighty Thor is cast out of Asgard to live on Earth, where he becomes one of the world\'s greatest heroes.',
        'content': 'Thor, the Norse god of thunder, is banished to Earth as punishment for his reckless actions in Asgard. As he learns humility, he discovers the true meaning of being a hero and must protect Earth from the villainous Loki and the impending destruction from the Frost Giants.'
    }
]



def starting_page(request):
    return render(request, 'netflix/index.html', {
        'featured_movies': movies
    })

def all_movies_page(request):
    return render(request, 'netflix/all_movies.html', {
        'all_movies_list': movies
    })  

