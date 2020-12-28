// main.js

// console.log('Hello Team Penguin (from main.js)');

console.log('test (from main.js)');
// Sidebar functionality modified from https://www.w3schools.com/howto/howto_js_collapse_sidebar.asp
/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openNav() {
	console.log('open (from main.js)');
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

// Sidebar functionality modified from https://www.w3schools.com/howto/howto_js_collapse_sidebar.asp
/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
	console.log('close (from main.js)');
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}