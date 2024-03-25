const burger = document.querySelector('.burger');
const nav = document.querySelector('.header__nav');
burger.addEventListener('click', () => {
    burger.classList.toggle('burger__active');
    nav.classList.toggle('header__nav-active')
    if(!burger.classList.contains('burger__active') && !nav.classList.contains('header__nav-active')) {
        document.body.style.overflow = 'auto'
        return
    }
    document.body.style.overflow = 'hidden'
})
