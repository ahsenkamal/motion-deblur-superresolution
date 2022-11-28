const iutLocationSearchButtonClicked = async (event) => {
  const iutLocationNode = document.getElementById('iut-location');
  const value = await askForFile();
  if (value != null) {
    iutLocationNode.value = value;
    doMotionDeblur(value);
  }
}

const slidersChanged = async () => {
  let imagePath = document.getElementById('iut-location').value;
  let angle = document.getElementById('angle-slider').value;
  let d = document.getElementById('strength-slider').value;
  let snr = document.getElementById('snr-slider').value;

  doMotionDeblur(imagePath, Number.parseInt(angle), Number.parseInt(d), Number.parseInt(snr), true);
}

const angleSliderInput = async (event) => {
  document.getElementById('angle-slider-display').innerText = document.getElementById('angle-slider').value;
  slidersChanged();
}

const strengthSliderInput = async (event) => {
  document.getElementById('strength-slider-display').innerText = document.getElementById('strength-slider').value;
  slidersChanged();
}

const snrSliderInput = async (event) => {
  document.getElementById('snr-slider-display').innerText = document.getElementById('snr-slider').value;
  slidersChanged();
}

const setupEvents = () => {
  document.getElementById('iut-location-search').addEventListener('click', iutLocationSearchButtonClicked);
  document.getElementById('angle-slider').addEventListener('input', angleSliderInput);
  document.getElementById('strength-slider').addEventListener('input', strengthSliderInput);
  document.getElementById('snr-slider').addEventListener('input', snrSliderInput);
}