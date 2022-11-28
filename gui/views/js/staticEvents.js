const iutLocationSearchButtonClicked = async (event) => {
  const iutLocationNode = document.getElementById('iut-location');
  const value = await askForFile();
  if (value != null) {
    iutLocationNode.value = value;
  }
}

const motionDeblurButtonClicked = async (event) => {
  window.location = "motion_deblur.html";
}

const superResButtonClicked = async (event) => {
  window.location = "super_resolution.html";
}

const setupEvents = () => {
  document.getElementById('iut-location-search').addEventListener('click', iutLocationSearchButtonClicked);
  document.getElementById('motion-deblur-button').addEventListener('click', motionDeblurButtonClicked);
  document.getElementById('super-res-button').addEventListener('click', superResButtonClicked);
}