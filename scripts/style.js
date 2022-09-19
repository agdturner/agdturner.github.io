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
 
 /**
 * Function to initialise the style sheet for code.
 */
function initStyle() {
    console.log('initStyle()');
	var dark_theme = "/tools/highlight/styles/github-dark.min.css";
	var light_theme = "/tools/highlight/styles/github.min.css";
	var theme = localStorage.getItem("theme");
	var css = localStorage.getItem("css");
	console.log('theme=' + theme);
	if (theme == null) {
		console.log('theme == null');
		theme = light_theme;
		localStorage.setItem("theme", light_theme);
		localStorage.setItem("antitheme", dark_theme);
		localStorage.setItem("theme_name", "Light Mode");
		localStorage.setItem("antitheme_name", "Dark Mode");
		css = "/css/style_light.css";
		localStorage.setItem("css", "/css/style_light.css");
		localStorage.setItem("anticss", "/css/style_dark.css");
	} else {
		//var element = document.body;
		//element.classList.add("dark-mode");
		//element.classList.add("button2");
		if (theme === dark_theme) {
			console.log('theme === dark_theme');
		} else {
			console.log('theme === light_theme');
			//element.classList.toggle("dark-mode");
			//element.classList.toggle("button2");
		}
	}
	console.log('theme=' + theme);
	console.log('antitheme=' + localStorage.getItem("antitheme"));
	document.getElementById('code_theme').setAttribute('href', theme);
	document.getElementById("style_button").innerHTML = localStorage.getItem("antitheme_name");
	document.getElementById('css').setAttribute('href', css);
}

/**
 * Function to change from light mode to dark mode and vice versa.
 */
function swapStyle(){
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