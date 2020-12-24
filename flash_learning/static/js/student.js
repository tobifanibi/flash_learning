console.log('Hello student! (from student.js)');

var navbar_open = false;

// Sidebar functionality modified from https://www.w3schools.com/howto/howto_js_collapse_sidebar.asp
/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openNav() {

	if (!navbar_open) {
		console.log('opened');
		document.getElementById("mySidebar").style.width = "250px";
		document.getElementById("main").style.marginLeft = "250px";
		navbar_open = true;
		console.log('navbar_open is now', navbar_open);
	} else {
		closeNav();

	}
	
}

// Sidebar functionality modified from https://www.w3schools.com/howto/howto_js_collapse_sidebar.asp
/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
	console.log('closed');
	document.getElementById("mySidebar").style.width = "0";
	document.getElementById("main").style.marginLeft = "0";
	navbar_open = false;
}