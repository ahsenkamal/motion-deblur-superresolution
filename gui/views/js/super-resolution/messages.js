eel.expose(displayIUTforSuperResolution);
function displayIUTforSuperResolution(message) {
    const iutNode = document.getElementById('iut');
    iutNode.src = message;
}

eel.expose(displayOUTforSuperResolution);
function displayOUTforSuperResolution(message) {
    const outNode = document.getElementById('out');
    outNode.src = message;
}
