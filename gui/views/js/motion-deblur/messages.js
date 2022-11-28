eel.expose(displayIUT);
function displayIUT(message) {
    const iutNode = document.getElementById('iut');
    iutNode.src = message;
}
