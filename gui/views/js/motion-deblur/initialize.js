class PanZoomElement {
  constructor(el, img) {
    this.scale = 1;
    this.panning = false;
    this.point = {x: 0, y: 0};
    this.start = {x: 0, y: 0};
    this.el = el;
    this.img = img;

    this.calculateCenter();
    this.setupEventHandlers();
  }

  calculateCenter() {
    this.center = {
      x: this.el.offsetLeft + this.el.offsetWidth/2,
      y: this.el.offsetTop + this.el.offsetHeight/2,
    };
  }

  setupEventHandlers() {
    this.el.onmousedown = (e) => {
      e.preventDefault();
      this.start = {x: e.clientX-this.center.x-this.point.x, y: e.clientY-this.center.y-this.point.y};
      this.panning = true;
    }

    this.el.onmouseup = (e) => {
      this.panning = false;
    }

    this.el.onmousemove = (e) => {
      e.preventDefault();
      if (!this.panning) return;

      this.point.x = e.clientX - this.center.x - this.start.x;
      this.point.y = e.clientY - this.center.y - this.start.y;
      this.setTransform();
    }

    this.el.onwheel = (e) => {
      e.preventDefault();
      let xs = (e.clientX - this.center.x - this.point.x) / this.scale,
          ys = (e.clientY - this.center.y - this.point.y) / this.scale,
          delta = (e.wheelDelta ? e.wheelDelta : -e.deltaY);
      
      (delta > 0) ? (this.scale *= 1.2) : (this.scale /= 1.2);
      this.point.x = e.clientX - this.center.x - xs * this.scale;
      this.point.y = e.clientY - this.center.y - ys * this.scale;

      this.setTransform();
    }
  }

  setTransform() {
    this.img.style.transform = `translate(${this.point.x}px, ${this.point.y}px) scale(${this.scale})`
  }
}

panzoom_els = []

function setupImagesPanZoom() {
  let iut_zoom = document.getElementById('iut-zoom');
  let iut = document.getElementById('iut');
  panzoom_els.push(new PanZoomElement(iut_zoom, iut));

  let out_zoom = document.getElementById('out-zoom');
  let out = document.getElementById('out');
  panzoom_els.push(new PanZoomElement(out_zoom, out));
}

window.addEventListener("load", async () => {
  setupEvents();

  setupImagesPanZoom();

  doMotionDeblur(); // first de-blur with default values

  // If the server stops, close the UI
  window.eel._websocket.addEventListener('close', e => window.close());
});

window.addEventListener("resize", async () => {
  panzoom_els.forEach(el => el.calculateCenter());
});
