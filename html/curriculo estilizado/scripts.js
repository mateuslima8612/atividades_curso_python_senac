// 1. criar função de trocar bg
// 2. pegar o botao pelo id 



document.getElementById("botao-bg").onclick= setInterval(changeBackground, 1000)


function changeBackground(){
    let element = document.querySelector("body");
    let footerElement = document.querySelector("footer")
    const footerColor = window.getComputedStyle(footerElement).backgroundColor;
    if (footerColor === "rgb(0, 0, 0)") {
        footerElement.style.backgroundColor = "rgb(255, 255, 255)";
        element.style.backgroundImage = "url(./bg.jpg)"
    }
    else if(footerColor === "rgb(255, 255, 255)") {
        footerElement.style.backgroundColor = "rgb(0, 0, 0)";
        element.style.backgroundImage = "url(./greenbg.jpg)"
    }

}

var clock = document.getElementById('clock')

function time() {
    var d = new Date();
    var s = d.getSeconds();
    var m = d.getMinutes();
    var h = d.getHours();
    clock.textContent = 
      ("0" + h).substr(-2) + ":" + ("0" + m).substr(-2) + ":" + ("0" + s).substr(-2);
  }
  
setInterval(time, 1000);

