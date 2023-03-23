function ChartModule() {

    const canvas = document.querySelector("#chart");

    if(canvas){
    const ctx = canvas.getContext("2d");
    const selectList = document.querySelector(".stat-select-list");
    const selectBtn = document.querySelector("#stat-btn");
    const width = 500;
    const height = 500;
    let data;
    canvas.style.cssText = `width: ${width}px; height: ${height}px; background: #d9d9d9; border-radius: 15px;`;
    canvas.width = width;
    canvas.height = height;

    async function chartDB() {
        await fetch(`/api/v1/graph?coin=${selectList.value}`, {
            method: "GET",
            headers: {
                "content-type" : "application/json"
            }
        })
        .then(response => response.json())
        .then(res => {
            data = res;
        })

        const renderChart = (data) => {

        let x = data.map(item => item[0]);
        let currX = x.length;
        ctx.font = "bold 10px 'Rubik', sans-serif";

        for (let i = 0; i < currX; i++) {
            ctx.fillText(x[i], 17 + i * 69, 475);
        }

        let y = data.map((elem, i) =>{
            return elem[1];
        })

        let dp = y[1] / 40;

        ctx.fillStyle = "#35068C";

        for (let i = 0; i < currX; i++) {
            ctx.fillRect(25 + i * 67, 460 - y[i] / dp * 5, 50, y[i] / dp * 5);
        }

        ctx.fillStyle = "#35068C";
        ctx.lineWidth = 2.0;
        ctx.beginPath();
        ctx.moveTo(0, 460);
        ctx.lineTo(500, 460);
        ctx.stroke();

        ctx.fillStyle = "#35068C";
        ctx.strokeStyle = "#878787"

        for(let i = 0; i <= y.length; i++){
            ctx.fillText((y[i]) + "$", 29 + i * 67, 455 - y[i] / dp * 5);
            ctx.beginPath();
            ctx.stroke();
        }

        ctx.font = "bold 30px 'Rubik', sans-serif";
        ctx.fillText(selectList.value + "", 10, 50);
            ctx.beginPath();
            ctx.stroke();

    };

    renderChart(data);
    }

    chartDB()

    selectBtn.addEventListener("click", (e) => {
        e.preventDefault();

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        chartDB();

    })
    }

}

export default ChartModule;