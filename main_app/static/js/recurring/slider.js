$(document).ready(function () {
    if (window.innerWidth <= 992) {
      $(".portfolio__list").slick({
        arrows: false,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
      });
    }
    if (window.innerWidth <= 992) {
      $(".employer__list").slick({
        arrows: false,
        infinite: true,
        variableWidth: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
      });
    }
    $(".blog__list-item-slider").slick({
      arrows: false,
      infinite: false,
      variableWidth: true,
      slidesToShow: 1,
      slidesToScroll: 1,
      dots: true,
      centerMode: true,
      centerPadding: '0px'
    });
});
