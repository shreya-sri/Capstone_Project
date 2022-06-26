function faceVideo() {
    eel.face_video()()
}

function aadharVideo() {
    eel.aadhar_video()()
}


eel.expose(updateImageSrc);
function updateImageSrc(val) {
    let elem = document.getElementById('bg');
    elem.src = "data:image/jpeg;base64," + val
}

eel.expose(nextPage);
function nextPage() {
    let elem = document.getElementById('next');
    elem.click()

}

eel.expose(restart);
function restart(){
    let elem = document.getElementById('next');
    elem.href="detect_face.html";
    elem.click()
}
