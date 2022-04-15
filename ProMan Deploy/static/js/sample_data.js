// It is just an idea how you can structure your data during your page is running.
// You can use it for testing purposes by simply copy/paste/run in the Console tab in your browser

let keyInLocalStorage = 'proman-data';

let sampleData = {
    "statuses": [
        {
            "id": 1,
            "name": "New"
        },
        {
            "id": 2,
            "name": "In progress"
        },
        {
            "id": 3,
            "name": "Testing"
        },
        {
            "id": 4,
            "name": "Done"
        }
    ],
    "boards": [
        {
            "id": 1,
            "title": "Test Board 1",
            "is_active": true
        },
        {
            "id": 2,
            "title": "Test Board 2",
            "is_active": true
        }
    ],
    "cards": [
        {
            "id": 1,
            "title": "task1",
            "board_id": 1,
            "status_id": 1,
            "order": 3
        },
        {
            "id": 2,
            "title": "task2",
            "board_id": 1,
            "status_id": 2,
            "order": 2
        },
        {
            "id": 3,
            "title": "task3",
            "board_id": 1,
            "status_id": 4,
            "order": 1
        },
        {
            "id": 4,
            "title": "task4",
            "board_id": 2,
            "status_id": 1,
            "order": 3
        },
        {
            "id": 5,
            "title": "task5",
            "board_id": 2,
            "status_id": 2,
            "order": 2
        },
        {
            "id": 6,
            "title": "task6",
            "board_id": 2,
            "status_id": 3,
            "order": 1
        }
    ]
};

localStorage.setItem(keyInLocalStorage, JSON.stringify(sampleData));

