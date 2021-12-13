function move() {
    var elem = document.getElementById("myBar");   
    var txt = document.querySelector(".progress_bar p");
    var x = document.getElementById("c_btn");
    var width = 0;
    var id = setInterval(frame, 50);
    function frame() {
        if (width >= 100) {
          clearInterval(id);
          x.style.display = "inline-block";
          x.click();
        } 
        else {
            width++; 
            elem.style.width = width + '%'; 
            txt.innerHTML = width * 1  + '%';
        }
    }
}
setTimeout(move, 2000);

function img1_hover() {
    var ele = document.getElementById("voice_yes");
    ele.addEventListener("mouseenter", function() {
        var img = document.querySelector("#voice_yes img")
        img.src = "images/speaker_black.png";
    }, false );
    ele.addEventListener("mouseleave", function() {
        var img = document.querySelector("#voice_yes img")
        img.src = "images/speaker_white.png";
    }, false );
}

function img2_hover() {
    var ele = document.getElementById("voice_no");
    ele.addEventListener("mouseenter", function() {
        var img = document.querySelector("#voice_no img")
        img.src = "images/keyboard_black.png";
    }, false );
    ele.addEventListener("mouseleave", function() {
        var img = document.querySelector("#voice_no img")
        img.src = "images/keyboard_white.png";
    }, false );
}

function enable_voice_yes() {
    localStorage.setItem("activate_voice", "yes");
}

function enable_voice_no() {
    localStorage.setItem("activate_voice", "no");
}


