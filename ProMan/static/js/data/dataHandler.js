export let dataHandler = {
    getBoards: async function () {
        return await apiGet("/api/boards");
    },
    getStatuses: async function () {
        return await apiGet(`api/statuses`);
    },
    getCardsByBoardId: async function (boardId) {
        return await apiGet(`/api/boards/${boardId}/cards/`);
    },
    createNewCard: async function (cardTitle, boardId, statusId) {
        return await apiPost(`/api/${boardId}/${statusId}/${cardTitle}`);
    },
    renameBoard: async function(boardId, boardTitle) {
        await apiPost(`/rename-board-by-id/${boardId}/${boardTitle}`)
    },
    renameColumn: async function(statusId, columnTitle) {
        await apiPost(`/rename-column-by-id/${statusId}/${columnTitle}`)
    },
    renameCard: async function(cardId, cardTitle) {
        await apiPost(`/rename-card-by-id/${cardId}/${cardTitle}`)
    },
    deleteSpecificCard: async function(cardId) {
        await apiPost(`/delete-card/${cardId}`)
    },
    addBoard: async function (boardTitle){
        await apiPost(`/add-board/${boardTitle}`)
    },
    getNewCardData: async function (){
        return await apiGet(`/api/new-card`)
    },
    getMaxId: async function (){
        return await apiGet(`/api/max-id`)
    },
    deleteBoard: async function (boardId){
        await apiPost(`/api/delete-board/${boardId}`)
    },
    addNewColumn: async function () {
        await apiPost(`/api/add-new-column`)
    },
    newColumnData: async function () {
        return apiGet('/api/new-column')
    },
    getAllBoardsIds: async function () {
        return apiGet('/api/all-boards-ids')
    },
    deleteSpecificColumn: async function (columnId) {
        return apiPost(`/api/delete-column/${columnId}`)
    },
    swapCards: async function (card1,card2){
        await apiPost(`/api/swap/${card1}/${card2}`)
    },
    newCardPos: async function (col,card,board_id){
        await apiPost(`/api/newCardPos/${col}/${card}/${board_id}`)
    },
    addNewPrivateBoard: async function (title){
        await apiPost(`/api/new-private-board/${title}`)
    },
    getLowestStatusId: async function (){
        return await apiGet(`/api/lowest-status-id`)
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

async function apiPost(url) {
    await fetch(url, {
        method: 'POST',
    })
}
