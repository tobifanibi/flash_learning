
// Create new line chart using chart.js
new Chart(document.getElementById("line-chart"), {
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
        borderColor: "#3e95cd",
        fill: false
      }
    ]
  },

  // Add an overall title to the line graph
  options: {
    title: {
      display: true,
      text: 'Number of Successful Flaschcards Learned Per Month'
    }
  }
});