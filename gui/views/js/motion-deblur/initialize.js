let adderNames;
let currentAdder;

window.addEventListener("load", async () => {
  setupEvents();

  doMotionDeblur(); // first de-blur with default values

  // If the server stops, close the UI
  window.eel._websocket.addEventListener('close', e => window.close());
});
