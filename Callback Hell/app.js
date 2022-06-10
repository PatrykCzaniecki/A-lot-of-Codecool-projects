let count = 6;
let content = document.getElementById('outputText');
content.innerText = 'The bomb goes off in...';
setTimeout(() => {
    count--;
    content.innerText = count + '...';
    setTimeout(() => {
        count--;
        content.innerText = count + '...';
        setTimeout(() => {
            count--;
            content.innerText = count + '...';
            setTimeout(() => {
                count--;
                content.innerText = count + '...';
                setTimeout(() => {
                    count--;
                    content.innerText = count + '...';
                    setTimeout(() => {
                        count--;
                        content.innerText = 'Boom!!!';
                        setTimeout(() => {
                            content.innerText = 'The bomb exploded!💣!💣!';
                            }, 1000);
                        }, 1000);
                    }, 1000);
                }, 1000);
            }, 1000);
        }, 1000);
    }, 1000);
