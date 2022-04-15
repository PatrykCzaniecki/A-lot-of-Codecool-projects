function init() {
    let characters = document.getElementsByClassName('actor_details');
    for (let character of characters) {
        character.addEventListener('click', showAllActors);
    }
};

async function showAllActors(clickEvent){
    let actorId = clickEvent.target.id;
    let actorDetails = await dataHandler.getActor(actorId);
    let divElement = document.getElementsByClassName(`${actorId}`)[0];
    let pElement = document.createElement('p');
    pElement.innerText = `${actorDetails.name}` + ' ---> ' + `${actorDetails.birthday}`;
    divElement.appendChild(pElement);
}

let dataHandler = {
    getActor: async function (actorId) {
        return await apiGet(`/actor/${actorId}`);
    }
};

async function apiGet(url) {
    let response = await fetch(url, {
        method: "GET",
    });
    if (response.ok) {
        return await response.json();
    }
}

window.onload = function () {
    init();
}