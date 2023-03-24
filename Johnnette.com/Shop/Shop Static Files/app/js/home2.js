// Initialize Swiper2
var swiper = new Swiper(".mySwiper1", {
    slidesPerView: 5,
    spaceBetween: 0,
    freeMode: true,
    // loop: true,
    grabCursor: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    breakpoints: {
        1441: {
            slidesPerView: 7,
        },
        975: {
            slidesPerView: 5,
        },
        768: {
            slidesPerView: 4,
        },
        500: {
            slidesPerView: 3,
        },
        290: {
            slidesPerView: 2,
        },
    },
});