let searchBtn = document.querySelector('#search-btn');
let searchBar = document.querySelector('.search-bar-container');
let formBtn = document.querySelector('#register-btn');
let registerForm = document.querySelector('.register-form-container');
let formClose = document.querySelector('#form-close');
let menu = document.querySelector('#menu-bar');
let navbar = document.querySelector('.navbar');
/*let videoBtn = document.querySelectorAll('.vid-btn');*/
var video1 = document.getElementById('video1');
var video2 = document.getElementById('video2');
var video3 = document.getElementById('video3');
var video4 = document.getElementById('video4');
var video5 = document.getElementById('video5');

video1.onended = function () {
    video2.play();
    video1.style.opacity=0;
    video2.style.opacity=1;
}
video2.onended = function () {
    video3.play();
    video2.style.opacity=0;
    video3.style.opacity=1;
}
video3.onended = function () {
    video4.play();
    video3.style.opacity=0;
    video4.style.opacity=1;
}
video4.onended = function () {
    video5.play();
    video4.style.opacity=0;
    video5.style.opacity=1;
}
video5.onended = function () {
    video1.play();
    video5.style.opacity=0;
    video1.style.opacity=1;
}




window.onscroll = () =>{
    searchBtn.classList.remove('fa-times');
    searchBar.classList.remove('active');
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
    registerForm.classList.remove('active');
}

menu.addEventListener('click', () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');

});

searchBtn.addEventListener('click', () =>{
    searchBtn.classList.toggle('fa-times');
    searchBar.classList.toggle('active');

});

formBtn.addEventListener('click', () =>{
    registerForm.classList.add('active');

});

formClose.addEventListener('click', () =>{
     registerForm.classList.remove('active');

});



const scrollRevealOption = { 
    distance: "50px",
    origin: "bottom",
    duration: 1000,
};

ScrollReveal().reveal(".content .main-header", scrollRevealOption);

ScrollReveal().reveal(".content .sub-header", {
    ...scrollRevealOption,
    delay:500,
});

ScrollReveal().reveal(".content .btn", {
    ...scrollRevealOption,
    delay:1000,
    
});



/*videoBtn.forEach(btn =>{
    btn.addEventListener('click', ()=>{
        document.querySelector('.controls .active').classList.remove('active');
        btn.classList.add('active');
        let src = btn.getAttribute('data-src');
        document.querySelector('#video-slider').src= src;
    });

});*/
