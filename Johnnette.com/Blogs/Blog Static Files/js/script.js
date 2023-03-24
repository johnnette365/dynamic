let menu = document.querySelector("#menu-bar");
let navbar = document.querySelector('.navbar2');
let other = document.querySelector("#other-informations")
let icons = document.querySelector('.fab-icons')

menu.onclick = () => {
    menu.classList.toggle('fa-times')
    navbar.classList.toggle('active')
    other.classList.toggle('active')
    icons.classList.toggle('active')
}

// window.onclick = () => {
//     menu.classList.remove('fa-times')
//     navbar.classList.remove('active')
//     other.classList.remove('active')
// }

// document.onclick = function (e) {
//     if (e.target.id !== 'other-informations' && e.target.id !== 'menu-bar') {
//         if (e.target.offsetParent && e.target.offsetParent.id !== 'other-informations')
//             closeNav()
//     }
// }





// let button1 = document.querySelector('#button1')
// let submenu1 = document.querySelector('#sub-menu-1')
// button1.onclick = () => {
//     button1.classList.toggle('fa-angle-double-up')
//     submenu1.classList.toggle('active')
// }

// let button2 = document.querySelector('#button2')
// let submenu2 = document.querySelector('#sub-menu-2')
// button2.onclick = () => {
//     button2.classList.toggle('fa-angle-double-up')
//     submenu2.classList.toggle('active')
// }

// let button3 = document.querySelector('#button3')
// let submenu3 = document.querySelector('#sub-menu-3')
// button3.onclick = () => {
//     button3.classList.toggle('fa-angle-double-up')
//     submenu3.classList.toggle('active')
// }





// to remove header and header-background

let prevScrollPos = window.pageYOffset
const header = document.querySelector(".header")
const background = document.querySelector(".header_background")
const show = "show"
const with_background = "show_background"
window.onscroll = () => {
    const currentScrollPos = window.pageYOffset
    const halfScreenHeight = Math.floor(window.innerHeight / 2)

    menu.classList.remove('fa-times')
    navbar.classList.remove('active')
    other.classList.remove('active')

    if (currentScrollPos > halfScreenHeight) {
        background.classList.add(with_background)
    } else {
        background.classList.remove(with_background)
    }

    if (currentScrollPos > prevScrollPos) {
        header.classList.remove(show)
        console.log('scolling down')
    } else {
        header.classList.add(show)
        console.log("scolling up")
    }
    prevScrollPos = currentScrollPos
}