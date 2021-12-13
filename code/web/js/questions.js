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
        var btn = document.getElementsByClassName("next-button")[0];
        var div_btn = document.createElement('div');
        div_btn.classList.add("next-button");
        div_btn.innerHTML = "Submit";
        var link = document.createElement('a');
        link.appendChild(div_btn);
        var prnt = btn.parentNode;
        prnt.replaceChild(link, btn);
        link.setAttribute('onclick', 'temp_fix()')
    } 
    else {
        document.getElementsByClassName("next-button")[0].innerHTML = "Next";
    }
}
  
async function temp_fix() {
    var item = localStorage.getItem("activate_voice");
    var x = document.getElementsByClassName("tab");
    var c = document.getElementsByClassName("show")[0];
    var currentTab = parseInt(c.id);
    if (!validate_form(c)) {
        // var question = c.querySelector("h1");
        // eel.ReadQuestion(question.innerHTML)();
        if (item == "yes") {
            read_question();
        }
        return false;
    }
    else {
        var confirmed = 1;
        var lang = localStorage.getItem("language");
        if (item == "yes") {
            confirmed = await confirm_response(c);
            if (confirmed == 0) {
                response = c.querySelectorAll("#response");
                if (response.length == 1) {
                    response[0].value = "";
                }
                else {
                    for(var i=0; i<response.length; i++){
                        response[i].checked = "";
                    }
                }
                read_question();
            }
            else {
                window.location.assign("show_responses.html");
            }
            //eel.print_terminal("confirmed:"+confirmed)
        }
        if (currentTab == x.length-1 && confirmed == 1) {
            window.location.assign("show_responses.html");
        }
    }
}

async function next_prev(n) {
    var item = localStorage.getItem("activate_voice");
    var x = document.getElementsByClassName("tab");
    var c = document.getElementsByClassName("show")[0];
    var currentTab = parseInt(c.id);
    if (n == -1) {
        x[currentTab].style.display = "none";
        c.classList.remove("show");
        //console.log(currentTab);
        show_tab(currentTab-1);
    }
    else {
        if (n == 1 && !validate_form(c)) {
            // var question = c.querySelector("h1");
            // eel.ReadQuestion(question.innerHTML)();
            if (item == "yes") {
                read_question();
            }
            return false;
        }
        else {
            var confirmed = n;
            if (item == "yes") {
                confirmed = await confirm_response(c);
                //eel.print_terminal("confirmed:"+confirmed)
            }
            if (currentTab == x.length-1 && confirmed == 1) {
                //document.getElementById("regForm").submit();
                /*eel.FormResponsesPage();
                //eel.sleep(1);
                document.getElementsByClassName("next-button")[0].querySelector("a");
                eel.print_terminal(link.href);
                console.log("link accessed"); 
                eel.sleep(5);
                link.click();*/
                //return false;
            }
            else {
                if (confirmed == 0) {
                    response = c.querySelectorAll("#response");
                    if (response.length == 1) {
                        response[0].value = "";
                    }
                    else {
                        for(var i=0; i<response.length; i++){
                            response[i].checked = "";
                        }
                    }
                    read_question();
                }
                else {
                x[currentTab].style.display = "none";
                currentTab = currentTab + confirmed;
                c.classList.remove("show");
                //console.log(currentTab);
                show_tab(currentTab);
                }
            }
        }
    }
}

function display_responses() {
    var form = document.getElementById("regForm");
    var btn = document.getElementsByClassName("next-button")[0];
    var link = document.createElement('a');
    link.href = "show_responses.html";
    link.appendChild(btn);
    form.appendChild(link);
    
    //ink.click;
}

async function show_responses() {
    var prnt = document.querySelector("table");
    var response_dict = await eel.GetResponses()();
    var lang = localStorage.getItem("language");
    for (var i in response_dict) {
        var row = document.createElement("tr");
        var row_item1 = document.createElement("td");
        var row_item2 = document.createElement("td");
        question = document.createElement("h1");
        response = document.createElement("h1");
        question.style.cssText = "color: #66fcf1; font-size: 1.5625vw;";
        response.style.cssText = "color: #66fcf1; font-size: 1.5625vw;";
        question.innerHTML = i;
        if (lang == 1) {
            response.innerHTML = await eel.TranslateText(response_dict[i])();
        }
        else {
            response.innerHTML = response_dict[i];
        }
        row_item1.appendChild(question);
        row_item2.appendChild(response);
        row.appendChild(row_item1);
        row.appendChild(row_item2);
        prnt.appendChild(row);
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
        eel.SendData(question.innerHTML, y[0].title);
    }
    
    return valid; 
}

async function read_question() {
    var item = localStorage.getItem("activate_voice");
    var next = document.getElementsByClassName("next-button")[0];
    if (item == "yes") {
        var tab = document.getElementsByClassName("show")[0];
        var question = tab.querySelector("h1");
        var response = tab.querySelectorAll("#response");
        const responses = [];
        var lang = localStorage.getItem("language");
        if (lang == 0) {
            eel.ReadQuestion(question.innerHTML)();
            if (response[0].value != "" && !(response[0].type == "radio" || response[0].type == "checkbox")) {
                next.click();
                return;
            }
            if (response[0].type == 'date') {
                eel.ReadQuestion("Please respond in year, month, day format");
            }
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
            while (val == 0) {
                eel.ReadQuestion("Invalid response");
                var val = await eel.ListenResponse()();
            }
        }
        else {
            eel.ReadQuestion_kannada(question.innerHTML)();
            if (response[0].value != "" && !(response[0].type == "radio" || response[0].type == "checkbox")) {
                next.click();
                return;
            }
            if (response[0].type == 'date') {
                eel.ReadQuestion_kannada("ವರ್ಷ, ತಿಂಗಳು, ದಿನ ಸ್ವರೂಪದಲ್ಲಿ ಪ್ರತಿಕ್ರಿಯಿಸಿ");
            }
            if (response[0].type == "radio" || response[0].type == "checkbox") {
                for (var i=0; i<response.length; i++) {
                    responses.push(response[i].value);
                }
                eel.ReadQuestion_kannada("ಆಯ್ಕೆಗಳು ಇವೆ");
                eel.ReadQuestion_kannada(responses.toString());
            }    
            else if (response[0].localName == "select" && (question.innerHTML.includes("State") == false && question.innerHTML.includes("City") == false)) {
                for (var i=0; i<response[0].options.length; i++) {
                    responses.push(response[0].options[i].value);
                }
                eel.ReadQuestion_kannada("ಆಯ್ಕೆಗಳು ಇವೆ");
                eel.ReadQuestion_kannada(responses.toString());
            }
            
            var val = await eel.ListenResponse()();
            while (val == 0) {
                eel.ReadQuestion_kannada("ಅಮಾನ್ಯ ಪ್ರತಿಕ್ರಿಯೆ");
                var val = await eel.ListenResponse()();
            }
        }
        fill_responses(val);
    }
}

async function fill_responses(val) {
    var tab = document.getElementsByClassName("show")[0];
    var y = tab.querySelectorAll("#response");
    var next = document.getElementsByClassName("next-button")[0];
    if (y[0].localName == "input") {
        if (y[0].type == "text" || y[0].type == "email" || y[0].type == "number" || y[0].type == "date") {
            y[0].value = val;
            next.click();
        }
        else if (y[0].type == "radio") {
            for (var i = 0; i < y.length; i++) {
                if (y[i].value.toLowerCase() == val) {
                    y[i].checked = true;
                    next.click();
                }
            }
        }
        else if (y[0].type == "checkbox") {
            for (var i = 0; i < y.length; i++) {
                var check = await eel.CheckBox(y[i].value.toLowerCase(), val)();
                if (check == 1) {
                    y[i].checked = true;
                }
            }
            next.click();
        }
    }
    else if (y[0].localName == "select") {
        for (var i = 0; i < y[0].options.length; i++) {
            if (val == y[0].options[i].value.toLowerCase()) {
                y[0].options[i].selected = true;
                next.click();
            }
        }
    }
    else if (y[0].localName == "textarea") {
        y[0].value = val;
        next.click();
    }
}

async function confirm_response(c) {
    y = c.querySelectorAll("#response");
    var response;
    if (y[0].localName == "input") {
        if (y[0].type == "text" || y[0].type == "email" || y[0].type == "number" || y[0].type == "date") {
            response = y[0].value;
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
            response = responses.toString();
        }
    }
    else if (y[0].localName == "select") {
        response = y[0].options[y[0].selectedIndex].value   
    }
    else if (y[0].localName == "textarea") {
        response = y[0].value;
    }
    /*else if (y[0].localName == "video") {
        valid = false;
    }
    else if (y[0].localName == "img") { 
    }*/
    var n=0; //If n is 0 it stays on the same page. If n is 1 it goes to the next page.
    var lang = localStorage.getItem("language");
    if (lang == 0) {
        eel.ReadQuestion("Confirm response? " + response);
        var res = await eel.ListenResponse()();
    }
    else {
        eel.ReadQuestion_kannada("ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ದೃಢೀಕರಿಸಿ? " + response);
        var res = await eel.ListenResponse_kannada()();
    }
    //eel.print_terminal("in confirm_response:"+res+n);
    if (!res){
        return 0
    }
    if (!res.includes("yes")) {
        n = 0;
    } 
    else {
        n = 1;
    } 
    return n;
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
        var title = video.title.replace(".", "");
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
                img.setAttribute("title", title);
                var link = document.createElement("a");
                link.setAttribute("download", title);
                link.href = dataURL;
                link.appendChild(img);
                link.click();
                
                eel.AddFile(title)

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
    modal.style.display = "block";
}

function close_popup() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
}

function submit_form() {
    //document.getElementById("regForm").submit();
    eel.SaveData();
    var lang = localStorage.getItem("language");
    if (lang == 0) {
        eel.ReadQuestion("Responses Submitted. Thank you");
        window.location.assign("detect_face.html");
    }
    else {
        eel.ReadQuestion_kannada("ಪ್ರತಿಸ್ಪಂದನಗಳು ಸಲ್ಲಿಸಲಾಗಿದೆ. ಧನ್ಯವಾದ.");
        window.location.assign("../detect_face.html");
    }

}