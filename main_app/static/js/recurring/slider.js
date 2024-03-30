$(document).ready(function() {
    if(window.innerWidth <= 992) {
        $('.portfolio__list').slick({
            arrows: false,
            infinite: true,
            slidesToShow: 1,
            slidesToScroll: 1
        });
    }
})