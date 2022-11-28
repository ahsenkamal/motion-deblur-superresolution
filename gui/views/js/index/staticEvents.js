const motionDeblurButtonClicked = async (event) => {
  window.location = "motion_deblur.html";
}

const superResButtonClicked = async (event) => {
  window.location = "super_resolution.html";
}

const setupEvents = () => {
  document.getElementById('motion-deblur-button').addEventListener('click', motionDeblurButtonClicked);
  document.getElementById('super-res-button').addEventListener('click', superResButtonClicked);
}