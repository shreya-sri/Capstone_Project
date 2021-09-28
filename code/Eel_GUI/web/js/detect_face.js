function py_video() {
    eel.video_feed()()
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

