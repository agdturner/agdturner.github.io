/**
 * Copyright 2022 Centre for Computational Geography.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
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
//    //alert("button is clicked");
//	swapStyle();
//});

/**
 * Function to initialise the style sheet for code.
 */
function initStyle() {
    console.log('initStyle()');
	var dark_theme = "/tools/highlight/styles/github-dark.min.css";
	var light_theme = "/tools/highlight/styles/github.min.css";
	var theme = localStorage.getItem("theme");
	var css = localStorage.getItem("css");
	// Check if the browser setting prefers dark.
	const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches
	console.log('prefersDarkMode ' + prefersDarkMode);
	if (prefersDarkMode) {
		theme = dark_theme;
		antitheme = light_theme;
		localStorage.setItem("theme_name", "Dark Mode");
		localStorage.setItem("antitheme_name", "Light Mode");
		localStorage.setItem("css", "/css/style_dark.css");
		localStorage.setItem("anticss", "/css/style_light.css");
	} else {
		theme = light_theme;
		antitheme = dark_theme;
		localStorage.setItem("theme_name", "Light Mode");
		localStorage.setItem("antitheme_name", "Dark Mode");
		localStorage.setItem("css", "/css/style_light.css");
		localStorage.setItem("anticss", "/css/style_dark.css");
	}
	localStorage.setItem("theme", theme);
	localStorage.setItem("antitheme", antitheme);	
	console.log('theme=' + theme);
	console.log('antitheme=' + localStorage.getItem("antitheme"));
	document.getElementById('code_theme').setAttribute('href', theme);
	document.getElementById("style_button").innerHTML = localStorage.getItem("antitheme_name");
	document.getElementById('css').setAttribute('href', css);
	// The following commented out line fails currently, but might be a better way:
	// var id = path.dirname(window.location.pathname).split(path.sep).pop();
	var dirs = window.location.pathname.split("/");
	var id = dirs[dirs.length - 2];
	console.log(id);
	var element = document.getElementById(id);
	element.style.outline = "thin solid green";
}

/**
 * Function to change from light mode to dark mode and vice versa.
 */
function swapStyle() {
	console.log('swapStyle');
	//var element = document.body;
	//element.classList.toggle("dark-mode");
	var theme = localStorage.getItem("antitheme");
	var antitheme = localStorage.getItem("theme");
	var theme_name = localStorage.getItem("antitheme_name");
	var antitheme_name = localStorage.getItem("theme_name");
	localStorage.setItem("theme", theme);
	localStorage.setItem("antitheme", antitheme);
	localStorage.setItem("theme_name", theme_name);
	localStorage.setItem("antitheme_name", antitheme_name);
	document.getElementById('code_theme').setAttribute('href', theme);
	document.getElementById("style_button").innerHTML = antitheme_name;
	console.log('theme=' + theme);
	console.log('antitheme=' + antitheme);
	var css = localStorage.getItem("anticss");
	var anticss = localStorage.getItem("css");
	localStorage.setItem("css", css);
	localStorage.setItem("anticss", anticss);
    document.getElementById("css").setAttribute("href", css);  
}

addEventListener('DOMContentLoaded', (event) => {
	initStyle();
	console.log('The DOM is fully loaded.');
});

addEventListener('load', (event) => {
	console.log('The page is fully loaded.');
});

//addEventListener('beforeunload', (event) => {
//	// show the confirmation dialog
//	event.preventDefault();
//	// Google Chrome requires returnValue to be set.
//	event.returnValue = '';
//});
//
//addEventListener('unload', (event) => {
//	// send analytic data
//});