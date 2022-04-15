function init() {
    let button = document.getElementById('year-submit')
    button.onclick = getActors;
}

async function getActors() {
    let yearFrom = document.getElementById('year-from')
    let yearTo = document.getElementById('year-to')
    let yearFromValue = yearFrom.value
    let yearToValue = yearTo.value
    let data = await getActorsForTask(yearFromValue, yearToValue)
    for (let actor of data) {
        let name = document.createElement('p')
        let birthday = document.createElement('span')
        let card = document.getElementsByClassName('card')[0]
        name.textContent = actor.name + ' -- '
        birthday.textContent = actor.birthday
        name.appendChild(birthday)
        card.appendChild(name)
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

async function getActorsForTask(yearFrom, yearTo) {
    return await apiGet(`api/task/${yearFrom}/${yearTo}`);
}

window.onload = function () {
    init();
};