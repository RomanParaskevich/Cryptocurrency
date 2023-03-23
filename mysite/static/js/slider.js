"use strict";

function SliderModule() {

        const btnSlyderLeft = document.querySelector(".before-btn"),
          btnSlyderRight = document.querySelector(".after-btn"),
          slyderItemCard = document.querySelectorAll(".slider-cadr-item");
      
        let slyderCounter = 1;
      
        function slyderCardFun() {
      
          if (slyderCounter > slyderItemCard.length) {
            slyderCounter = 1;
          }
      
          if (slyderCounter < 1) {
            slyderCounter = slyderItemCard.length;
          }
      
          slyderItemCard.forEach(item => {
            return item.style.display = "none"
          });
      
          slyderItemCard[slyderCounter - 1].style.display = 'block';
        }
      
        slyderCardFun(slyderCounter);
      
      
        btnSlyderLeft.addEventListener("click", (e) => {
          e.preventDefault();
          slyderCounter += 1;
          slyderCardFun();
        })
      
        btnSlyderRight.addEventListener("click", (e) => {
          e.preventDefault();
          slyderCounter -= 1;
          slyderCardFun();
        })
}

export default SliderModule;