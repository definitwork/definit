const item = document.querySelectorAll('.expertise__list-item') || []


item.forEach((el) => {
    el.addEventListener('click', () => {
        el.classList.toggle('expertise__item-active')  
    })
})
