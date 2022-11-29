const slidersChanged = async () => {
  let angle = document.getElementById('angle-slider').value;
  let d = document.getElementById('strength-slider').value;
  let snr = document.getElementById('snr-slider').value;

  doMotionDeblur(Number.parseInt(angle), Number.parseInt(d), Number.parseInt(snr), true);
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

const saveButtonClicked = async (event) => {
  askAndSaveImage(document.getElementById('out').src);
}

const setupEvents = () => {
  document.getElementById('angle-slider').addEventListener('input', angleSliderInput);
  document.getElementById('strength-slider').addEventListener('input', strengthSliderInput);
  document.getElementById('snr-slider').addEventListener('input', snrSliderInput);
  document.getElementById('save-button').addEventListener('click', saveButtonClicked);
}