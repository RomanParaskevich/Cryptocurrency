"use strict";

function CalculateModule() {
    const form = document.querySelector(".calculate-form-block"),
    formBtn = document.querySelector(".calculate-btn"),
    hashRate = document.querySelector("#hash-rate"),
    calculateSelect = document.querySelector("#calculate-select-list"),
    estimated = document.querySelector(".cur-mon"),
    currency = document.querySelector(".currency"),
    dollars = document.querySelector(".dollars");

    form.addEventListener("submit", (e) => {
        e.preventDefault();

            async function calculateRequest() {

                await fetch(`/api/v1/calculate?hash=${hashRate.value}&coin=${calculateSelect.value}`, {
                    method: "GET",
                    headers: {
                        "content-type": "application/json"
                    }
                })
                .then(response => {
                    if (response.ok == false) alert("Произошла ошибка!");

                    return response.json()
                })
                .then(res => {
                    currency.textContent = res[0];
                    estimated.textContent = res[1];
                    dollars.textContent = res[2];

                })
            }
            calculateRequest();
    })
}

export default CalculateModule;