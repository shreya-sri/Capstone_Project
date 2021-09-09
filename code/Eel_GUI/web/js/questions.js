async function all_questions() {
    var prnt = document.getElementById("regForm");
    prnt.classList.add("animated");
    prnt.classList.add("fadeInTop");
    var num = await eel.get_num()();
    for (var j=num; j>=0; j--) {
        var tab = document.createElement("div");
        tab.classList.add("tab");
        if (j == 0) {
            tab.style.display = "block";
            tab.classList.add("show");
        }
        tab.id = String(j);
        tab.classList.add("animated");
        tab.classList.add("fadeInTop");
        prnt.insertBefore(tab, prnt.firstChild);
        var txt = await eel.get_question(j)();
        q = document.createElement("h1");
        q.id = "question";
        q.style.cssText = "color: #66fcf1; font-size: 50px; text-align: center;";
        if (txt == "") {
            question = "Thank you!";
            q.innerHTML = question;
            tab.appendChild(q);
        }
        else {
            var question = txt[0];
            q.innerHTML = question;
            tab.appendChild(q);
            var response = txt[1].split(':');
            if (response.length == 1) {
                if (response[0] == "multi_textbox") {
                    var m = document.createElement('textarea');
                    m.classList.add("txtbox");
                    m.classList.add("use-keyboard-input");
                    m.id = "response";
                    m.style.height = '200px';
                    tab.appendChild(m);
                }
                else if (response[0] == "camera") {
                    var m = document.createElement('video');
                    m.classList.add('p');
                    m.style.cssText = "color: #66fcf1; font-size: 60px; text-align: center;";
                    m.innerHTML = "Camera";
                    m.id = "response";
                    tab.appendChild(m);
                }
                else {
                    var m = document.createElement('input');
                    if (response[0] == "textbox") {
                        m.setAttribute('type', 'text');
                    }
                    else if (response[0] == "email") {
                        m.setAttribute('type', 'email');
                    }
                    else if (response[0] == "number") {
                        m.setAttribute('type', 'number');
                    }
                    else if (response[0] == "date") {
                        m.setAttribute('type', 'date');
                    }
                    if (question.includes("required") == true) {
                        m.setAttribute('required', true);
                    } 
                    m.classList.add("txtbox");
                    m.classList.add("use-keyboard-input");
                    m.id = "response";
                    tab.appendChild(m);
                }
            }
            else {
                if (response[0] == "radio") {
                    var vals = response[1].split('/')
                    var options = vals[1].split(',');
                    var name = vals[0];
                    for (var i=0; i<options.length; i++) {
                        var m = document.createElement('input');
                        m.setAttribute('type', 'radio');
                        m.setAttribute('name', name);
                        m.setAttribute('value', options[i]);
                        m.setAttribute('required', true);
                        var label = document.createElement('label');
                        label.style.cssText = "color: #ffffff; font-size: 20px; text-align: center;";
                        label.classList.add("label-radio");
                        label.innerHTML = options[i];
                        tab.appendChild(label);
                        label.appendChild(m);
                    }
                }
                else if (response[0] == "dropdown") {
                    var vals = response[1].split('/')
                    var options = vals[1].split(',');
                    var name = vals[0];
                    var m = document.createElement('select');
                    m.setAttribute('name', name);
                    m.setAttribute('required', true);
                    m.classList.add('dropdown');
                    for (var i=0; i<options.length; i++) {
                        o = document.createElement('option');
                        o.setAttribute('value', options[i]);
                        o.style.cssText = "color: #000000; font-size: 20px; text-align: center;";
                        o.innerHTML = options[i];
                        m.appendChild(o);
                    }
                    tab.appendChild(m);
                }
                else if (response[0] == "checkbox") {
                    var vals = response[1].split('/')
                    var options = vals[1].split(',');
                    var name = vals[0];
                    for (var i=0; i<options.length; i++) {
                        var m = document.createElement('input');
                        m.setAttribute('type', 'checkbox');
                        m.setAttribute('name', name);
                        m.setAttribute('value', options[i]);
                        m.setAttribute("required", true);
                        var label = document.createElement('label');
                        label.style.cssText = "color: #ffffff; font-size: 20px; text-align: center;";
                        label.classList.add("label-checkbox");
                        label.innerHTML = options[i];
                        tab.appendChild(label);
                        label.appendChild(m);
                    }
                }
            }
        }
    }
}


function showTab(n) {
    var nbtn = document.getElementsByClassName("next-button")[0];
    var pbtn = document.getElementsByClassName("prev-button")[0];
    nbtn.classList.add("animated");
    nbtn.classList.add("fadeInTop");
    pbtn.classList.add("animated");
    pbtn.classList.add("fadeInTop");
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    x[n].classList.add("show");
    //console.log(x[n].id);
    if (n == 0) {
        document.getElementsByClassName("prev-button")[0].style.display = "none";
    } else {
        document.getElementsByClassName("prev-button")[0].style.display = "inline";
    }
    if (n == (x.length - 1)) {
        document.getElementsByClassName("next-button")[0].innerHTML = "Submit";
    } 
    else {
        document.getElementsByClassName("next-button")[0].innerHTML = "Next";
    }
}
  
function nextPrev(n) {
    var nbtn = document.getElementsByClassName("next-button")[0];
    var pbtn = document.getElementsByClassName("prev-button")[0];
    nbtn.classList.remove("animated");
    nbtn.classList.remove("fadeInTop");
    pbtn.classList.remove("animated");
    pbtn.classList.remove("fadeInTop");
    var x = document.getElementsByClassName("tab");
    var c = document.getElementsByClassName("show")[0];
    var currentTab = parseInt(c.id);
    console.log(currentTab);
    if (n == 1 && !validateForm(c)) {
        return false;
    }
    x[currentTab].style.display = "none";
    currentTab = currentTab + n;
    c.classList.remove("show");
    //console.log(currentTab);
    if (currentTab >= x.length) {
        document.getElementById("regForm").submit();
        return false;
    }
    showTab(currentTab);
}
  
function validateForm(c) {
    var y, i, valid = true;
    y = c.getElementsByTagName("input");
    if (y.length == 1) {
        if (y[0].value == "" && y[0].required == true) {
            //console.log("false");
            //y[i].className += " invalid";
            valid = false;
        }
    }
    
    return valid; 
}

function get_video() {
    var video = document.getElementsByClassName('video')[0];
    // Get access to the camera!
    if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        // Not adding `{ audio: true }` since we only want video now
        navigator.mediaDevices.getUserMedia({ video: true }).then(function() {
        //video.src = window.URL.createObjectURL(stream);
        // Avoid using this in new browsers, as it is going away.
            const mediaStream = navigator.mediaDevices.getUserMedia({video: true});
            video.srcObject = mediaStream;
            video.play();
        });
    }
}