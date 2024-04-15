const reelsItem = document.querySelectorAll('.reels__list-item') || []


reelsItem.forEach(item => {
    item.addEventListener('click', (e) => {
        console.log(e.currentTarget);
    })
})