import {dataHandler} from "../data/dataHandler.js";
import {htmlFactory, htmlTemplates} from "../view/htmlFactory.js";
import {domManager} from "../view/domManager.js";
import {refresh} from "../main.js";

let counter
let archive = false;
const showArchiveBtn = document.getElementById('archive');
showArchiveBtn.addEventListener('click', async function (){await showArchive()});
const hideArchiveBtn = document.getElementById('hide-archive');
hideArchiveBtn.addEventListener('click', async function (){await hideArchive()});

export let cardsManager = {
    loadCards: async function (boardId) {
        const statuses = await dataHandler.getStatuses(boardId);
        const cards = await dataHandler.getCardsByBoardId(boardId);
        for (let column of statuses) {
            const columnBuilder = htmlFactory(htmlTemplates.status)
            const columnsContent = columnBuilder(column, boardId)
            domManager.addChild(`.board-columns[data-board-id="${boardId}"]`, columnsContent);
            domManager.addEventListener(`.board-column-title[data-column-id="${boardId}${column.id}"]`, "click", changeColumnTitle)
            domManager.addEventListener(`.column-remove[data-remove-status-id="${boardId}${column.id}"]`, "click", removeColumn)
            for (let card of cards) {
                if (card.status_id === column.id && archive == false) { if (card.archive == 'false') {
                    const cardBuilder = htmlFactory(htmlTemplates.card);
                    const content = await cardBuilder(card, column);
                    domManager.addChild(`.board-column-content[data-column-id="${boardId}${column.id}"]`, content);
                    domManager.addEventListener(`.card-remove[data-remove-card-id="${card.id}"]`, "click", deleteButtonHandler);

                    document.querySelector(`.card[data-card-id='${card.id}']`).removeEventListener("dblclick", await changeCardTitle)
                    domManager.addEventListener(`.card[data-card-id='${card.id}']`, "dblclick", await changeCardTitle)
                    let archiveBtn = document.getElementById(`archive${card.id}`)
                    archiveBtn.addEventListener('click',async function (){archiveCard(card.id,card.board_id)})
                }
                }
                else if (card.status_id === column.id && archive==true) { if (card.archive == 'true') {

                    await hideBoardButtons ()
                    const cardBuilder = htmlFactory(htmlTemplates.card);
                    const content = await cardBuilder(card, column, archive);
                    domManager.addChild(`.board-column-content[data-column-id="${boardId}${column.id}"]`, content);
                    domManager.addEventListener(`.card-remove[data-remove-card-id="${card.id}"]`, "click", deleteButtonHandler);
                    document.querySelector(`.card[data-card-id='${card.id}']`).removeEventListener("dblclick", await changeCardTitle)
                    domManager.addEventListener(`.card[data-card-id='${card.id}']`, "dblclick",await changeCardTitle);
                    let unarchiveBtn = document.getElementById(`unarchive${card.id}`);
                    unarchiveBtn.addEventListener('click',async function (){unarchiveCard(card.id,card.board_id)})
                }
                }
            }
        }
        await findCards()
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
    counter = 0
    let cardId = clickEvent.target.dataset.cardId;
    let element = document.querySelector(`.card[data-card-id='${cardId}']`);

        if (document.getElementById(`archive${cardId}`)) {
            document.getElementById(`archive${cardId}`).style.display = 'none'
            document.getElementById(`archive${cardId}`).innerText = ''
        }else {
            document.getElementById(`unarchive${cardId}`).style.display = 'none'
            document.getElementById(`unarchive${cardId}`).innerText = ''
        }
        document.getElementById(`x${cardId}`).innerText = ''
        element.contentEditable = true
        element.draggable = false

    if (counter === 0) {
        element.addEventListener('focusout', await async function () {
            console.log('funkcja działa')
            let title = element.textContent
            // if (title.slice(-7,-1) === "archive") {
            //     title = title.slice(0, -7)
            // }
            if (title == '') {
                element.textContent = 'no name'
                title = 'no name'
            }

            element.contentEditable = false
            element.draggable = true

            await dataHandler.renameCard(cardId, title)
            let boardId = element.title
            counter ++
            let btn = document.querySelector(`.toggle-board-button[data-board-id="${boardId}"]`)
            await btn.click()
            await btn.click()
        })
    }


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
    let dropzoneID = e.currentTarget.id
    const draggableID = e.dataTransfer.getData('text/plain');
    let boardID = document.getElementById(draggableID).title

    await dataHandler.newCardPos(dropzoneID,draggableID,boardID);
    clearCards((boardID-1))
}

async function dropCard(e){
    await eventRemove()
    let dropzoneID = e.currentTarget.id
    const draggableID = e.dataTransfer.getData('text/plain');
    let boardID = document.getElementById(draggableID).title

    await dataHandler.swapCards(dropzoneID,draggableID);
    clearCards((boardID-1))
}

export async function clearCards (boardID){
    console.log ('clear')
    let btn = document.querySelectorAll('.toggle-board-button')
    let counter = 0
    while (counter<2){
            await btnClick(boardID)
            counter++
    }
}

export async function btnClick(i){
    let btn = document.querySelector(`.toggle-board-button[data-board-id="${i+1}"]`)
    setTimeout((await btn.click()),3000)
}

async function archiveCard (cardID, boardID) {

    dataHandler.archive(cardID)
    clearCards(boardID-1)
}
async function unarchiveCard (cardID, boardID) {

    dataHandler.unarchive(cardID)
    clearCards(boardID-1)
}
async function showArchive(){
    archive = true
    await refresh()
    document.querySelectorAll('.board-add').forEach(e => e.remove())
    document.querySelectorAll('.board-delete').forEach(e => e.remove())
    document.querySelectorAll('.add-column').forEach(e => e.remove())
    showArchiveBtn.style.display = 'none'
    hideArchiveBtn.style.display = 'inline-block'
    document.body.style.background = '#8D8D8DFF'
}

async function hideArchive(){
    archive = false
    refresh()
    showArchiveBtn.style.display = 'inline-block'
    hideArchiveBtn.style.display = 'none'
    document.body.style.background =  "#ddd url(http://cdn.backgroundhost.com/backgrounds/subtlepatterns/diagonal-noise.png)"
}

function hideBoardButtons (){}
    // let addBtns = document.getElementsByClassName('board-add')
    // let deleteBtns = document.getElementsByClassName()