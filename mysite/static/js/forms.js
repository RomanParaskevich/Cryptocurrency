"use strict";

function FormsModule() {
    const loginBtn = document.querySelector(".header-login-link"),
  registerBtn = document.querySelector(".header-register"),
  modalWindow = document.querySelector(".modal"),
  modalForm = document.querySelector(".modal__form"),
  modalLogin = document.querySelector(".modal__form_login"),
  modalPass = document.querySelector(".modal__form_register"),
  loginFormBtn = document.querySelector("#form-login-btn"),
  regFormBtn = document.querySelector("#reg-btn"),
  headerLoggout = document.querySelector("#header-loggout"),
  headerRegister = document.querySelector("#header-register");
  const div = document.createElement("div");

const addElemBlock = (state) => {
  div.className = "backdrop";
  document.body.append(div);
}

const removeElemBlock = () => {
  div.remove();
}

const addModal = () => {
  modalWindow.classList.add("modal_active");
  addElemBlock();

}

const closeModal = () => {
  modalWindow.classList.remove("modal_active");
}

const loginEvent = (e) => {
  e.preventDefault();
  addModal();
  modalLogin.style.display = "flex";
}

if(loginBtn){loginBtn.addEventListener("click", loginEvent);}

if(headerLoggout){headerLoggout.addEventListener("click", loginEvent);}


const registerEvent = (e) => {
  e.preventDefault();
  addModal();
  modalPass.style.display = "flex";
}

if(registerBtn){registerBtn.addEventListener("click", registerEvent);}

if(headerRegister){headerRegister.addEventListener("click", registerEvent);}

document.addEventListener("keydown", (e) => {
  if (e.code === "Escape") {
    modalLogin.style.display = "none";
    modalPass.style.display = "none";
    closeModal();
    removeElemBlock();
  }

})

const formValueReset = (form => form.reset());


}

export default FormsModule;