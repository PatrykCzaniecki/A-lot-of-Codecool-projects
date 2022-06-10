import {boardsManager} from "./controller/boardsManager.js";
import {removeAllBoards} from "./controller/boardsManager.js";
import {domManager} from "./view/domManager.js";


function init() {
    console.log("x")
    boardsManager.loadBoards();
    domManager.addEventListener("#refresh", "click", refresh)

}

export async function refresh() {
    removeAllBoards()
    await boardsManager.loadBoards();
}

init();
