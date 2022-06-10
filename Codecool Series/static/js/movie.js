function init() {
    let button = document.getElementById('movie-submit');
    button.onclick = getActors;
}

async function getActors() {
    let title = document.getElementById('movie-input');
    let titleValue = title.value;
    let data = await getActorsForMovie(titleValue);
    for (let actor of data) {
        let name = document.createElement('p');
        let biography = document.createElement('span');
        let card = document.getElementById('movie-card');
        name.textContent = actor[0].name + ' -- '
        biography.textContent = actor[0].biography
        name.appendChild(biography);
        card.appendChild(name);
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

async function getActorsForMovie(titleValue) {
    return await apiGet(`api/movie/${titleValue}`);
}

window.onload = function () {
    init();
};