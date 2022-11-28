function setupImagesPanZoom() {
  let iut_frame = document.getElementById('iut-frame');
  WZoom.create('#iut', {
    dragScrollableOptions: {
      onGrab: function () {
        iut_frame.style.cursor = 'grabbing';
      },
      onDrop: function () {
        iut_frame.style.cursor = 'grab';
      }
    }
  });

  let out_frame = document.getElementById('out-frame');
  WZoom.create('#out', {
    dragScrollableOptions: {
      onGrab: function () {
        out_frame.style.cursor = 'grabbing';
      },
      onDrop: function () {
        out_frame.style.cursor = 'grab';
      }
    }
  });
}

window.addEventListener("load", async () => {
  setupEvents();

  // setupImagesPanZoom();

  doMotionDeblur(); // first de-blur with default values

  // If the server stops, close the UI
  window.eel._websocket.addEventListener('close', e => window.close());
});
