async function all_questions() {
    var prnt = document.getElementById("regForm");
    prnt.classList.add("animated");
    prnt.classList.add("fadeInTop");
    var num = await eel.GetNum()();
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
        var txt = await eel.GetQuestion(j)();
        q = document.createElement("h1");
        q.id = "question";
        q.style.cssText = "color: #66fcf1; font-size: 3.125vw; text-align: center;";
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
                    m.style.height = '12.5vw';
                    tab.appendChild(m);
                }
                else if (response[0] == "camera") {
                    var m = document.createElement('video');
                    m.classList.add('video');
                    m.setAttribute('width', 240);
                    m.setAttribute('height', 180);
                    m.setAttribute('autoplay', '');
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
                        label.style.cssText = "color: #ffffff; font-size: 1.25vw; text-align: center;";
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
                        o.style.cssText = "color: #000000; font-size: 1.25vw; text-align: center;";
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
                        label.style.cssText = "color: #ffffff; font-size: 1.25vw; text-align: center;";
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


function show_tab(n) {
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    x[n].classList.add("show");
    //console.log(n);
    //console.log(x.length-1);
    //var question = x[n].getElementsByTagName("h1")[0];
    add_cities(x[n]);
    get_video(x[n]);
    capture_image(x[n]);
    read_question();
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
  
function next_prev(n) {
    var x = document.getElementsByClassName("tab");
    var c = document.getElementsByClassName("show")[0];
    var currentTab = parseInt(c.id);
    if (n == 1 && !validate_form(c)) {
        //var question = c.querySelector("h1");
        //eel.ReadQuestion(question.innerHTML)();
        return false;
    }
    if (currentTab == x.length-1) {
        //document.getElementById("regForm").submit();
        open_popup();
        //return false;
    }
    else {
        x[currentTab].style.display = "none";
        currentTab = currentTab + n;
        c.classList.remove("show");
        //console.log(currentTab);
        show_tab(currentTab);
    }
}
  
function validate_form(c) {
    var y, valid = true;
    question = c.querySelector("h1");
    y = c.querySelectorAll("#response");
    if (y[0].localName == "input") {
        if (y[0].type == "text" || y[0].type == "email" || y[0].type == "number" || y[0].type == "date") {
            if (y[0].value == "" && y[0].hasAttribute('required')) {
                //console.log("false");
                //y[i].className += " invalid";
                valid = false;
            }
            else {
                eel.SendData(question.innerHTML, y[0].value);
            }
        }
        else if (y[0].type == "radio" || y[0].type == "checkbox") {
            var len = 0;
            const responses = [];
            for (var i = 0; i < y.length; i++) {
                if (y[i].checked == true) {
                    len ++; 
                    responses.push(y[i].value);     
                }
            }
            if (len == 0) {
                valid = false;
            }
            else {
                eel.SendData(question.innerHTML, responses.toString());
            }
        }
    }
    else if (y[0].localName == "select") {
        if (y[0].options[y[0].selectedIndex].value == "") {
            valid = false;
        }
        else {
            eel.SendData(question.innerHTML, y[0].options[y[0].selectedIndex].value);
        }
    }
    else if (y[0].localName == "textarea") {
        eel.SendData(question.innerHTML, y[0].value);
    }
    else if (y[0].localName == "video") {
        valid = false;
    }
    else if (y[0].localName == "img") {
        eel.SendData(question.innerHTML, y[0].src);
    }
    
    return valid; 
}

async function read_question() {
    var item = localStorage.getItem("activate_voice");
    if (item == "yes") {
        var tab = document.getElementsByClassName("show")[0];
        var question = tab.querySelector("h1");
        var response = tab.querySelectorAll("#response");
        const responses = [];
        eel.ReadQuestion(question.innerHTML)();
        if (response[0].type == "radio" || response[0].type == "checkbox") {
            for (var i=0; i<response.length; i++) {
                responses.push(response[i].value);
            }
            eel.ReadQuestion("The options are");
            eel.ReadQuestion(responses.toString());
        }    
        else if (response[0].localName == "select" && (question.innerHTML.includes("State") == false && question.innerHTML.includes("City") == false)) {
            for (var i=0; i<response[0].options.length; i++) {
                responses.push(response[0].options[i].value);
            }
            eel.ReadQuestion("The options are");
            eel.ReadQuestion(responses.toString());
        }
        var val = await eel.ListenResponse()();
        console.log(val);
    }
}

function get_video(x) {
    var video = x.querySelector(".video");
    if (video != null) {
        if (video.localName == "video") {
            if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
                    video.srcObject = stream;
                    video.play();
                });
            }
        }
        else if (video.localName == "img") {
            var new_video = document.createElement("video");
            new_video.classList.add('video');
            new_video.setAttribute('width', 480);
            new_video.setAttribute('height', 360);
            new_video.setAttribute('autoplay', '');
            new_video.id = "response";
            if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
                    new_video.srcObject = stream;
                    new_video.play();
                });
            }
            video.parentNode.replaceChild(new_video, video);
        }
    }
}

function stop_video(video) {
    stream = video.srcObject;
    stream.getTracks().forEach(function(track) {
        if (track.readyState == 'live' && track.kind === 'video') {
            track.stop();
        }
    });
}

function capture_image(x) {
    var video = x.querySelector(".video");
    var p = x.querySelector("p");
    if (video != null) {
        document.addEventListener('keypress', event => {
            if (event.code === 'KeyC') {
                if (p!= null) {
                    p.parentNode.removeChild(p);
                }
                var scale = 1;
                var canvas = document.createElement("canvas");
                canvas.width = video.videoWidth * scale;
                canvas.height = video.videoHeight * scale;
                canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
                var dataURL = canvas.toDataURL("image/png");
                var img = document.createElement('img');
                img.classList.add("video");
                img.id = "response";
                img.src = dataURL;
                img.setAttribute("title", video.title);
                var link = document.createElement("a");
                link.setAttribute("download", video.title);
                link.href = dataURL;
                link.appendChild(img);
                link.click();
                
                eel.AddFile(video.title)

                stop_video(video);
                video.parentNode.replaceChild(link, video);
            }
        });
    }
}
    
async function add_cities(c) {
    if (c.querySelector("#response").name == "City") {
        var state = document.getElementsByName("State")[0];
        //console.log(state.name);
        var city = document.getElementsByName("City")[0];
        while (city.firstChild) {
            city.removeChild(city.lastChild);
        }
        var o = document.createElement('option');
        o.setAttribute('value', "");
        o.style.cssText = "color: rgb(0, 0, 0); font-size: 1.25vw; text-align: center;";
        o.innerHTML = "Select";
        city.appendChild(o);
        //console.log(state.options[state.selectedIndex].value)
        var x = state.options[state.selectedIndex].value;
        var cities = await eel.GetCities(x)();
        for (var i=0; i<cities.length; i++) {
            var o = document.createElement('option');
            o.setAttribute('value', cities[i]);
            o.style.cssText = "color: #000000; font-size: 1.25vw; text-align: center;";
            o.innerHTML = cities[i];
            city.appendChild(o);
        }
    }
}

function open_popup() {
    var modal = document.getElementById("myModal");
    var text = modal.querySelector(".modal-content p");
    var item = localStorage.getItem("activate_voice");
    if (item == "yes") {
        eel.ReadQuestion(text.innerHTML);
    }
    modal.style.display = "block";
}

function close_popup() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
}

function submit_form() {
    document.getElementById("regForm").submit();
    eel.SaveData();
    eel.DeleteTemp()();
}