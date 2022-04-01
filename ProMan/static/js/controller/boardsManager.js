import {dataHandler} from "../data/dataHandler.js";
import {htmlFactory, htmlTemplates, columnBuilder} from "../view/htmlFactory.js";
import {domManager} from "../view/domManager.js";
import {cardsManager} from "./cardsManager.js";
import {changeColumnTitle} from "./cardsManager.js";
import {deleteButtonHandler} from "./cardsManager.js";
import {changeCardTitle} from "./cardsManager.js";
import {removeColumn} from "./cardsManager.js";
import {findCards} from "./cardsManager.js";

export let boardsManager = {
    loadBoards: async function () {
        const boards = await dataHandler.getBoards();
        for (let board of boards) {
            const boardBuilder = htmlFactory(htmlTemplates.board);
            const content = boardBuilder(board);
            domManager.addChild("#root", content);
            domManager.addEventListener(`.board-title[data-title-id="${board.id}"]`, "click", changeBoardTitle)
            domManager.addEventListener(
                `.toggle-board-button[data-board-id="${board.id}"]`,
                "click",
                showHideButtonHandler
            );
            domManager.addEventListener(`.board-add[data-board-id="${board.id}"]`, "click", addNewCard);
            domManager.addEventListener(`.board-delete[data-board-id="${board.id}"]`, "click", deleteBoard);
            domManager.addEventListener(`.add-column[data-board-id="${board.id}"]`, "click", addColumn);
        }
    },
};

addNewBoard ()
addNewPrivateBoard()

function showHideButtonHandler(clickEvent) {
    const boardId = clickEvent.target.dataset.boardId;
    let button = document.querySelector(`.toggle-board-button[data-board-id="${boardId}"]`);
    if (button.innerText === "Show cards") {
        cardsManager.loadCards(boardId);
        button.innerText = "Hide cards";
    } else {
        let columns = document.querySelector(`.board-columns[data-board-id="${boardId}"]`);
        columns.remove();
        let content = `<div class="board-columns" data-board-id="${boardId}"></div>`
        domManager.addChild(`.board[data-board-id="${boardId}"]`, content);
        button.innerText = "Show cards";
    }
}

function changeBoardTitle(clickEvent) {
    const boardId = clickEvent.target.attributes['data-title-id'].nodeValue;
    let element = document.querySelector(`.board-title[data-title-id='${boardId}']`)
    let oldTitle = element.innerText
    element.addEventListener('focusout', async () => {
        let title = element.innerText
        if (title === '') {
            element.innerText = 'no name'
            await dataHandler.renameBoard(boardId, 'no name')
        } else if (title !== oldTitle || title === oldTitle) {
            await dataHandler.renameBoard(boardId, title)
        }
    })
}

async function addNewBoard (){
    let boardBtn = document.getElementById('new-board')
    boardBtn.addEventListener('click', async function (){
    let titleValue = "New board"
    await dataHandler.addBoard(titleValue)
        let lastID = await dataHandler.getMaxId()
        const boards = await dataHandler.getBoards();
        for (let board of boards) { if (board.id === lastID[0].max){
            const boardBuilder = htmlFactory(htmlTemplates.board);
            const content = boardBuilder(board);
            domManager.addChild("#root", content);
            domManager.addEventListener(`.board-title[data-title-id="${board.id}"]`, "click", changeBoardTitle)
            domManager.addEventListener(
                `.toggle-board-button[data-board-id="${board.id}"]`,
                "click",
                showHideButtonHandler);
            domManager.addEventListener(`.board-add[data-board-id="${board.id}"]`, "click", addNewCard);
            domManager.addEventListener(`.board-delete[data-board-id="${board.id}"]`, "click", deleteBoard);
            domManager.addEventListener(`.add-column[data-board-id="${board.id}"]`, "click", addColumn);
        }}})
        }

async function addNewCard(clickEvent) {
    let boardId = clickEvent.target.dataset.boardId;
    let button = document.querySelector(`.toggle-board-button[data-board-id="${boardId}"]`);
    let statusId = await dataHandler.getLowestStatusId();
    await dataHandler.createNewCard("New card", boardId, statusId[0].min);
    let newCardData = await dataHandler.getNewCardData()
    if (button.innerText === "Hide cards") {
        let content = `<div draggable="true" id="${newCardData[0].id}" title="${boardId}" class="card col${newCardData[0].status_id}" data-card-id="${newCardData[0].id}" contenteditable="true">${newCardData[0].title}
                    <div class="card-remove" data-remove-card-id="${newCardData[0].id}">x</div>
                </div>`;
        domManager.addChild(`.board-column-content[data-column-id="${newCardData[0].board_id}${newCardData[0].status_id}"]`, content);
        domManager.addEventListener(`.board-column-title[data-column-id="${newCardData[0].board_id}${newCardData[0].status_id}"]`, "click", changeColumnTitle)
        domManager.addEventListener(
            `.card-remove[data-remove-card-id="${newCardData[0].id}"]`,
            "click",
            deleteButtonHandler
        );
        domManager.addEventListener(`.card[data-card-id='${newCardData[0].id}']`, "click", changeCardTitle)
    }
     findCards()
}

async function deleteBoard(clickEvent) {
    let boardId = clickEvent.target.dataset.boardId;
    await dataHandler.deleteBoard(boardId);
    let board = document.querySelector(`.board-container[data-board-id="${boardId}"]`);
    board.remove();
}

async function addColumn(clickEvent) {
    let numberOfStatuses = await dataHandler.getStatuses()
    if (numberOfStatuses.length <= 6) {
        if (numberOfStatuses.length === 6) {
            let allButtons = document.getElementsByClassName(`add-column`);
            for (let button of allButtons) {
                button.innerText = "Can't add new column"
            }
        }
        await dataHandler.addNewColumn()
        let newColumn = await dataHandler.newColumnData()
        let allBoards = await dataHandler.getAllBoardsIds()
        for (let currentBoardId of allBoards) {
            let button = document.querySelector(`.toggle-board-button[data-board-id="${currentBoardId.id}"]`);
            if (button.innerText === "Hide cards") {
                let newId = currentBoardId.id;
                let newColumnContent = columnBuilder(newColumn[0], newId)
                domManager.addChild(`.board-columns[data-board-id="${currentBoardId.id}"]`, newColumnContent);
                domManager.addEventListener(`.column-remove[data-remove-status-id="${newId}${newColumn[0].id}"]`, "click", removeColumn)
                domManager.addEventListener(`.board-column-title[data-column-id="${newId}${newColumn[0].id}"]`, "click", changeColumnTitle)
            }
            findCards()
        }
    } else {
        let allButtons = document.getElementsByClassName(`add-column`);
        for (let button of allButtons) {
            button.innerText = "Can't add new column"
        }
    }
}

export function removeAllBoards() {
    document.querySelectorAll('.board-container').forEach(e => e.remove())
}


async function addNewPrivateBoard() {
    let button = document.getElementById('new-private-board')
    button.addEventListener('click', async function () {
        let newTitle = "New Private board"
        await dataHandler.addNewPrivateBoard(newTitle)
        let lastID = await dataHandler.getMaxId()
        const boards = await dataHandler.getBoards();
        for (let board of boards) {
            if (board.id === lastID[0].max) {
                const boardBuilder = htmlFactory(htmlTemplates.board);
                const content = boardBuilder(board);
                domManager.addChild("#root", content);
                domManager.addEventListener(`.board-title[data-title-id="${board.id}"]`, "click", changeBoardTitle)
                domManager.addEventListener(`.toggle-board-button[data-board-id="${board.id}"]`, "click", showHideButtonHandler);
                domManager.addEventListener(`.board-add[data-board-id="${board.id}"]`, "click", addNewCard);
                domManager.addEventListener(`.board-delete[data-board-id="${board.id}"]`, "click", deleteBoard);
                domManager.addEventListener(`.add-column[data-board-id="${board.id}"]`, "click", addColumn);
            }
        }
    })
}
