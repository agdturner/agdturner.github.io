/**
 * Copyright 2022 Centre for Computational Geography.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * @author Andy Turner
 */
 //import path from 'path'; // import does not seem to work even when script type set to module using 
 
///**
// * Use jquery to listen to style_button click.
// */
//$(document).on('click', '#style_button', function(){ 
// //alert("button is clicked");
// swapStyle();
//});
	
/**
 * Function to initialise the style sheet for code.
 */
function initStyle() {
	// Check if the browser setting prefers dark.
	const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches
	console.log('prefersDarkMode ' + prefersDarkMode);
	if (localStorage.getItem("theme_name") == null) {
		if (prefersDarkMode) {
			setDarkMode();
		} else {
			setLightMode();
		}
	} else {
		if (localStorage.getItem("theme_name") === "Light Mode") {
			setLightMode();
		} else {
			setDarkMode()
		}
	}
	setOutline();
}

function setDarkMode() {
	localStorage.setItem("theme_name", "Dark Mode");
	localStorage.setItem("css1", "/tools/highlight/styles/github-dark.min.css");
	localStorage.setItem("css2", "/css/style_dark.css");
	document.getElementById("style_button").innerHTML = "Light Mode";
}

function setLightMode() {
	localStorage.setItem("theme_name", "Light Mode");
	localStorage.setItem("css1", "/tools/highlight/styles/github.min.css");
	localStorage.setItem("css2", "/css/style_light.css");
	document.getElementById("style_button").innerHTML = "Dark Mode";
}


/**
 * Function to change from light mode to dark mode and vice versa.
 */
function swapStyle() {
	console.log('swapStyle');
	//var element = document.body;
	//element.classList.toggle("dark-mode");
	var theme_name = localStorage.getItem("theme_name");
	if (theme_name === "Light Mode") {
		setDarkMode()
	} else {
		setLightMode()
	}
	setOutline();
}

function setOutline() {
	var dirs = window.location.pathname.split("/");
	var id = dirs[dirs.length - 2];
	console.log(id);
	var element = document.getElementById(id);
	element.style.outline = "thin solid green";
}

addEventListener('DOMContentLoaded', (event) => {
	initStyle();
	console.log('The DOM is fully loaded.');
});

addEventListener('load', (event) => {
	console.log('The page is fully loaded.');
});

//addEventListener('beforeunload', (event) => {
// // show the confirmation dialog
// event.preventDefault();
// // Google Chrome requires returnValue to be set.
// event.returnValue = '';
//});
//
//addEventListener('unload', (event) => {
// // send analytic data
//});