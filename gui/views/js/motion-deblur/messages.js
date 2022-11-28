eel.expose(displayIUT);
function displayIUT(message) {
    const iutNode = document.getElementById('iut');
    iutNode.src = message;
}

eel.expose(displayOUT);
function displayOUT(message) {
    const outNode = document.getElementById('out');
    outNode.src = message;
}

eel.expose(displayPSF);
function displayPSF(message) {
    const psfNode = document.getElementById('psf');
    psfNode.src = message;
}
