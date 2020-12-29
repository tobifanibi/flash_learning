
// Create new line chart using chart.js
var ctx = document.getElementById("line-chart");

var myChart = new Chart(ctx, {

  // Set chart type to line
  type: 'line',
  data: {

  	// Separate vertical lines by months
    labels: ['January','February','March','April','May','June','July','August','September','October', 'November', 'December'],
    
    // Graph these datasets (could add more, possibly the average user?)
    datasets: [

    // Data for the current user
    { 
        data: [0,0,22,24,56,24,26,96,87,81, 56, 34],
        label: "Your Score",
        fill: false,
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }
    ]
  },

  // Add an overall title to the line graph
  options: {
    title: {
      display: true,
      text: 'Number of Successful Flaschcards Learned Per Month'
    }, 
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: false
        }
      }]
    },
    legend: {
      display: false,
    }
  }
});


