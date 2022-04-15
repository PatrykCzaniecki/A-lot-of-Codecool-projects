let button1 = document.getElementById('button-s1');
let button2 = document.getElementById('button-s2');
let button3 = document.getElementById('button-s3');

function init () {
    button1.onclick = getEpisodes1;
    button2.onclick = getEpisodes2;
    button3.onclick = getEpisodes3;
}

async function getEpisodes1() {
    document.querySelector('#value').innerHTML = '';
    let buttonValue1 = 18511;
    let data1 = await getEpisodesForSeason(buttonValue1)
    for (let episode of data1) {
        let title = document.createElement('p')
        let overview = document.createElement('span')
        let card = document.getElementsByClassName('card')[1]
        title.textContent = episode.title + ' -- '
        overview.textContent = episode.overview
        title.appendChild(overview)
        card.appendChild(title)
    }
}

async function getEpisodes2() {
    document.querySelector('#value').innerHTML = '';
    let buttonValue2 = 18512;
    let data2 = await getEpisodesForSeason(buttonValue2)
    for (let episode of data2) {
        let title = document.createElement('p')
        let overview = document.createElement('span')
        let card = document.getElementsByClassName('card')[1]
        title.textContent = episode.title + ' -- '
        overview.textContent = episode.overview
        title.appendChild(overview)
        card.appendChild(title)
    }
}

async function getEpisodes3() {
    document.querySelector('#value').innerHTML = '';
    let buttonValue3 = 18513
    let data3 = await getEpisodesForSeason(buttonValue3)
    for (let episode of data3) {
        let title = document.createElement('p')
        let overview = document.createElement('span')
        let card = document.getElementsByClassName('card')[1]
        title.textContent = episode.title + ' -- '
        overview.textContent = episode.overview
        title.appendChild(overview)
        card.appendChild(title)
    }
}

async function apiGet(url) {
    let response = await fetch(url, {
        method: "GET",
    });
    if (response.ok) {
        return await response.json();
    }
}

async function getEpisodesForSeason(seasonNumber) {
    return await apiGet(`api/penguins/${seasonNumber}`);
}

window.onload = function () {
    init();
};