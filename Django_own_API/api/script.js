const videosSection = document.getElementById('videos-info');
const url = 'http://127.0.0.1:8000/api/data';

const addToWebsite = (tag, content, whereToAdd) => {
    const htmlTag =document.createElement(tag);
    htmlTag.textContent = content;
    whereToAdd.append(htmlTag)
}

const getData = async () => {
    const response = await fetch(url);
    const data = await response.json();
    data.forEach(oneVideo => {
        addToWebsite('p', oneVideo.title, videosSection)
    })
}

getData();