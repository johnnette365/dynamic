let menu = document.querySelector("#menu");
let navbar = document.querySelector(".navbar");
let btn = document.querySelector(".user");

menu.onclick = () => {
    menu.classList.toggle('fa-times')
    navbar.classList.toggle('active')
    btn.classList.toggle('active')

    profile.classList.remove('fa-caret-up')
    about.classList.remove('active')
}



let profile = document.querySelector("#profile");
let about = document.querySelector('.about_user');

profile.onclick = () => {
    profile.classList.toggle('fa-caret-up')
    about.classList.toggle('active')

    menu.classList.remove('fa-times')
    navbar.classList.remove('active')
    btn.classList.remove('active')
}