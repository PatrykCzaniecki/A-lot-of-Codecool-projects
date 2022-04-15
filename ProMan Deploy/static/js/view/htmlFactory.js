export const htmlTemplates = {
    board: 1,
    card: 2,
    status: 3
}

export const builderFunctions = {
    [htmlTemplates.board]: boardBuilder,
    [htmlTemplates.card]: cardBuilder,
    [htmlTemplates.status]: columnBuilder
};

export function htmlFactory(template) {
    if (builderFunctions.hasOwnProperty(template)) {
        return builderFunctions[template];
    }
    console.error("Undefined template: " + template);
    return () => {
        return "";
    };
}

function boardBuilder(board) {
    if (board.statuses < 7) {
        return `<div class="board-container" data-board-id="${board.id}" >
                    <section class="board" data-board-id="${board.id}">
                        <div class="board-header" id="${board.id}"><span class="board-title" data-title-id="${board.id}" contenteditable="true">${board.title}</span>
                            <button class="board-add" data-board-id="${board.id}">Add Card</button>
                            <button class="board-delete" data-board-id="${board.id}">Delete Board</button>
                            <button class="add-column" data-board-id="${board.id}">Add Column</button>
                            <button class="toggle-board-button" data-board-id="${board.id}">Show cards</button>
                        </div>
                        <div class="board-columns" data-board-id="${board.id}"></div>
                    </section>
                </div>`
    } else {
        return `<div class="board-container" data-board-id="${board.id}">
                    <section class="board" data-board-id="${board.id}">
                        <div class="board-header" id="${board.id}"><span class="board-title" data-title-id="${board.id}" contenteditable="true">${board.title}</span>
                            <button class="board-add" data-board-id="${board.id}">Add Card</button>
                            <button class="board-delete" data-board-id="${board.id}">Delete Board</button>
                            <button class="add-column" data-board-id="${board.id}">Can't add new column</button>
                            <button class="toggle-board-button" data-board-id="${board.id}">Show cards</button>
                        </div>
                        <div class="board-columns" data-board-id="${board.id}"></div>
                    </section>
                </div>`
    }

}

async function cardBuilder(card, column, archive = false) {
    if (archive == true){
        return `<div draggable="true" id="${card.id}" title="${card.board_id}" class="card col${column.id}" style = "background-color:black" data-card-id="${card.id}" contenteditable="false">${card.title}
                <div class="card-remove" data-remove-card-id="${card.id}" id="x${card.id}">x</div>
                <button class="buttonArchive" id="unarchive${card.id}">undo archiving</button></div>
            `;}
    else {
        return `<div draggable="true" id="${card.id}" title="${card.board_id}" class="card col${column.id}" data-card-id="${card.id}" contenteditable="false">${card.title}
                <div class="card-remove" data-remove-card-id="${card.id}" id="x${card.id}">x</div>
                <button class="buttonArchive" id="archive${card.id}">archive</button></div></div>`;}
}

export function columnBuilder(column, boardId) {
    return `<div class="board-column" id="${column.id}"  title="${boardId}" data-column-id="${boardId}${column.id}" data-status-id="${column.id}">
                <div style="display: inline-block;" class="board-column-title" data-column-id="${boardId}${column.id}" data-status-id="${column.id}" contenteditable="true">${column.title}</div>
                <div style="display: inline-block; float: right; cursor: pointer;" class="column-remove" data-remove-column-id="${column.id}" data-remove-status-id="${boardId}${column.id}">x</div>
                <div class="board-column-content" data-column-id="${boardId}${column.id}"></div>
            </div>`
}