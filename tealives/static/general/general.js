// JavaScript source code
var loading = document.createElement("div");
var loading_sub = document.createElement("div");
loading.classList.add("loading");
loading_sub.classList.add("logo");
loading_sub.innerHTML = "Tealives";
loading_sub.style = "font-size: 18vh;background: #0664d3;height: fit-content;cursor: pointer;padding: 4vh 2vh;";
loading.appendChild(loading_sub);
loading.style = "width: 100%;position: absolute;height: 100%;left: 50%;transform: translate(-50%);display: flex;align-items: center;justify-content: center;background: rgba(21, 23, 40, 1) 0%;";
document.querySelector("body").appendChild(loading);

function pLoad(container) {
    document.querySelector("." + container).style.display = "flex";
    document.querySelector("body").removeChild(document.querySelector(".loading"));
}