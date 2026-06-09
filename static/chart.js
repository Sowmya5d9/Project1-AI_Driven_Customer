// Customer Segmentation Chart

const segmentCanvas = document.getElementById("segmentChart");

if(segmentCanvas){

new Chart(segmentCanvas, {

    type: "pie",

    data: {

        labels: [
            "Premium",
            "Regular",
            "Low Value"
        ],

        datasets: [{
            data: [35, 45, 20]
        }]
    },

    options: {

        responsive: true,

        plugins: {

            legend: {
                position: "bottom"
            }
        }
    }
});
}



// Churn Prediction Chart

const churnCanvas = document.getElementById("churnChart");

if(churnCanvas){

new Chart(churnCanvas, {

    type: "doughnut",

    data: {

        labels: [
            "Likely Stay",
            "Likely Churn"
        ],

        datasets: [{
            data: [85, 15]
        }]
    },

    options: {

        responsive: true,

        plugins: {

            legend: {
                position: "bottom"
            }
        }
    }
});
}



// Monthly Revenue Trend

const revenueCanvas = document.getElementById("revenueChart");

if(revenueCanvas){

new Chart(revenueCanvas, {

    type: "line",

    data: {

        labels: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ],

        datasets: [{

            label: "Revenue",

            data: [
                10000,
                12000,
                15000,
                13000,
                18000,
                22000
            ],

            tension: 0.4,

            fill: false
        }]
    },

    options: {

        responsive: true,

        plugins: {

            legend: {
                display: true
            }
        }
    }
});
}