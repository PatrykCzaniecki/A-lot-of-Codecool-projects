import {boardsManager} from "./controller/boardsManager.js";
import {removeAllBoards} from "./controller/boardsManager.js";
import {domManager} from "./view/domManager.js";


function init() {
    boardsManager.loadBoards();
    let refreshButton = document.getElementById('refresh');
    domManager.addEventListener("#refresh", "click", refresh)
}

function refresh() {
    removeAllBoards()
    boardsManager.loadBoards();
}

init();
