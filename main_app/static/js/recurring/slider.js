$(document).ready(function () {
  if (window.location.href === "http://127.0.0.1:8000/portfolio/") {
    if (window.innerWidth <= 992) {
      $(".portfolio__list").slick({
        arrows: false,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
      });
    }
  }
  if (window.location.href === "http://127.0.0.1:8000/team/") {
    if (window.innerWidth <= 992) {
      $(".employer__list").slick({
        arrows: false,
        infinite: true,
        variableWidth: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        dots:true,
      });
    }
  }
});
