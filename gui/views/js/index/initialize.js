let adderNames;
let currentAdder;

window.addEventListener("load", async () => {
  setupEvents();

  // If the server stops, close the UI
  window.eel._websocket.addEventListener('close', e => window.close());
});
