import {dataHandler} from "../data/dataHandler.js";
import {htmlFactory, htmlTemplates} from "../view/htmlFactory.js";
import {domManager} from "../view/domManager.js";

export let cardsManager = {
    loadCards: async function (boardId) {
        const statuses = await dataHandler.getStatuses();
        const cards = await dataHandler.getCardsByBoardId(boardId);
        for (let column of statuses) {
            const columnBuilder = htmlFactory(htmlTemplates.status)
            const columnsContent = columnBuilder(column, boardId)
            domManager.addChild(`.board-columns[data-board-id="${boardId}"]`, columnsContent);
            domManager.addEventListener(`.board-column-title[data-column-id="${boardId}${column.id}"]`, "click", changeColumnTitle)
            domManager.addEventListener(`.column-remove[data-remove-status-id="${boardId}${column.id}"]`, "click", removeColumn)
            for (let card of cards) {
                if (card.status_id === column.id) {
                    const cardBuilder = htmlFactory(htmlTemplates.card);
                    const content = cardBuilder(card, column);
                    domManager.addChild(`.board-column-content[data-column-id="${boardId}${column.id}"]`, content);
                    domManager.addEventListener(`.card-remove[data-remove-card-id="${card.id}"]`, "click", deleteButtonHandler);
                    domManager.addEventListener(`.card[data-card-id='${card.id}']`, "click", changeCardTitle)
                }
            }
        } await findCards()
    },
};

export async function deleteButtonHandler(clickEvent) {
    const cardId = clickEvent.target.dataset.removeCardId;
    let allCards = document.getElementsByClassName("card");
    for (let card of allCards) {
        if (card.dataset.cardId === cardId) {
            card.remove();
            break;
        }
    }
    await dataHandler.deleteSpecificCard(cardId)
}

export function changeColumnTitle(clickEvent) {
    let statusId = clickEvent.target.dataset.statusId;
    let elements = document.querySelectorAll(`.board-column-title[data-status-id='${statusId}']`);
    for (let element of elements) {
        element.addEventListener('focusout', async () => {
            let title = element.innerText
            if (title === '') {
                title = 'no name'
            }
            await dataHandler.renameColumn(statusId, title)
            let all_columns = document.querySelectorAll(`.board-column-title[data-status-id="${statusId}"]`);
            for (let column of all_columns) {
                column.innerText = title
            }
        })
    }
}

export async function changeCardTitle(clickEvent) {
    let cardId = clickEvent.target.dataset.cardId;
    let element = document.querySelector(`.card[data-card-id='${cardId}']`);
    element.addEventListener('focusout', async () => {
        let title = element.innerText
        if (title === '') {
            title = 'no name'
        }
        await dataHandler.renameCard(cardId, title)
    })
}

export async function removeColumn(clickEvent) {
    let columnId = clickEvent.target.dataset.removeColumnId
    await dataHandler.deleteSpecificColumn(columnId)
    document.querySelectorAll(`.board-column[data-status-id="${columnId}"]`).forEach(e => e.remove());
    let buttons = document.getElementsByClassName('add-column');
    for (let button of buttons) {
        if (button.innerText === "Can't add new column") {
            button.innerText = "Add column"
        }
    }
}

////// DRAG AND DROP ITEM:
export async function findCards(){
const item = document.querySelectorAll('.card');
const columns = document.querySelectorAll('.board-column');
for (let i=0;i<item.length;i++) {
    item[i].addEventListener('dragstart', dragStart)
    item[i].addEventListener('dragenter', dragEnter)
    item[i].addEventListener('dragover', dragOver);
    item[i].addEventListener('dragleave', dragLeave);
    item[i].addEventListener('drop', await dropCard);
};

for (let i=0;i<columns.length;i++){
    columns[i].addEventListener('dragenter', dragEnter)
    columns[i].addEventListener('dragover', dragOver);
    columns[i].addEventListener('dragleave', dragLeave);
    columns[i].addEventListener('drop', dropColumn);
}
}

function dragStart(e){
    e.currentTarget.classList.add('dragStart')
    e.dataTransfer.setData('text/plain', e.currentTarget.id);
}

async function eventRemove(){
    const columns = document.querySelectorAll('.board-column');
    for (let i=0;i<columns.length;i++){
    columns[i].removeEventListener('dragenter', dragEnter)
    columns[i].removeEventListener('dragover', dragOver);
    columns[i].removeEventListener('dragleave', dragLeave);
    columns[i].removeEventListener('drop', await dropColumn);}
}

function dragEnter(e) {
    e.preventDefault();
    e.target.classList.add('drag-enter');
}

function dragOver(e) {
    e.preventDefault();
    e.target.classList.add('drag-over');
}


function dragLeave(e) {
}

async function dropColumn(e) {
    console.log('column')
    let dropzoneID = e.currentTarget.id
    const draggableID = e.dataTransfer.getData('text/plain');
    let boardID = document.getElementById(draggableID).title
    await dataHandler.newCardPos(dropzoneID,draggableID,boardID);
    clearCards((boardID-1))
}

async function dropCard(e){
    console.log ('card')
    await eventRemove()
    let dropzoneID = e.currentTarget.id
    const draggableID = e.dataTransfer.getData('text/plain');
    let boardID = document.getElementById(draggableID).title
    await dataHandler.swapCards(dropzoneID,draggableID);
    clearCards((boardID-1))
}

async function clearCards (boardID){
    let btn = document.querySelectorAll('.toggle-board-button')
    let counter = 0
    while (counter<2){
        await btnClick(boardID)
        counter++
    }
}

async function btnClick(i){
    let btn = document.querySelector(`.toggle-board-button[data-board-id="${i+1}"]`)
    setTimeout((btn.click()),3000)
}
