eel.expose(displayIUTforSuperResolution);
function displayIUTforSuperResolution(message) {
    document.getElementById('iut-loader').style.display = "none";
    document.getElementById('iut-zoom').style.display = "flex";
    document.getElementById('iut').src = message;
}

eel.expose(displayOUTforSuperResolution);
function displayOUTforSuperResolution(message) {
    document.getElementById('out-loader').style.display = "none";
    document.getElementById('out-zoom').style.display = "flex";
    document.getElementById('out').src = message;
}

