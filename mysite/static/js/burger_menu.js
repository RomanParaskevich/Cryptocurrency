"use strict";

function BurgerMenu() {

    const burgerBtn = document.querySelector(".burger-button"),
    burgerMenu = document.querySelector(".burger-menu"),
    closeMenu = document.querySelector(".close-menu");

    if(burgerBtn){burgerBtn.addEventListener("click", (e) => {
        e.preventDefault();

        burgerMenu.style.display = "block";
    })}
    else{console.log("error burgerMenu")}

    if(closeMenu){closeMenu.addEventListener("click", (e) => {
        e.preventDefault();

        burgerMenu.style.display = "none";
    })}
    else{console.log("error burgerMenu")}

}

export default BurgerMenu;