const iutLocationSearchButtonClicked = async (event) => {
  const iutLocationNode = document.getElementById('iut-location');
  const value = await askForFile();
  if (value != null) {
    iutLocationNode.value = value;
  }
}

const validateAndSubmitImagePath = async () => {
  const imagePath = document.getElementById('iut-location').value;
  if (imagePath) {
    await submitIUTPath(imagePath);
    return true;
  } else {
    return false;
  }
}

const motionDeblurButtonClicked = async (event) => {
  let valid = await validateAndSubmitImagePath();
  if (!valid) {
    alert("Please choose the image to motion de-blur!");
    return;
  }
  window.location = "motion_deblur.html";
}

const superResButtonClicked = async (event) => {
  let valid = await validateAndSubmitImagePath();
  if (!valid) {
    alert("Please choose the image to super resolve!");
    return;
  }
  window.location = "super_resolution.html";
}

const setupEvents = () => {
  document.getElementById('iut-location-search').addEventListener('click', iutLocationSearchButtonClicked);
  document.getElementById('motion-deblur-button').addEventListener('click', motionDeblurButtonClicked);
  document.getElementById('super-res-button').addEventListener('click', superResButtonClicked);
}