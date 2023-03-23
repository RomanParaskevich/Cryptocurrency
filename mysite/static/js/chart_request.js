"use strict";

function ChartRequestTwo() {
  const btc = document.querySelectorAll(".btc"),
    eth = document.querySelectorAll(".eth"),
    ltc = document.querySelectorAll(".ltc"),
    btnUpdate = document.querySelector(".btn-upd"),
    changeBtc = document.querySelector(".change.btc"),
    changeEth = document.querySelector(".change.eth"),
    changeLtc = document.querySelector(".change.ltc");

    function styleChange(elem) {
      if(Number(elem.textContent) >= 0){
        elem.style.color = "green"
      }
      else{
        elem.style.color = "red"
      }

    }

  function addCoin(responseObj, elem) {

    elem.forEach((item, i) => {

      item.textContent = responseObj[i];
    })
    styleChange(changeBtc);
  styleChange(changeEth);
  styleChange(changeLtc);
  }

  async function dataBaseRequest() {
    const coin = await fetch("/api/v1/currency/", {
        method: "GET",
        headers: {
          "content-type": "application/json"
        }
      })
      .then((response) => response.json())
      .then(database => database);
      addCoin(coin.BTCUSDT, btc);
      addCoin(coin.ETHUSDT, eth);
      addCoin(coin.LTCUSDT, ltc);
  }
  dataBaseRequest();

  btnUpdate.addEventListener("click", e => {
    e.preventDefault();

    dataBaseRequest();
  })
}

export default ChartRequestTwo;