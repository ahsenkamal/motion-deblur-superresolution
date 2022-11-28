const iutLocationSearchButtonClicked = async (event) => {
  const iutLocationNode = document.getElementById('iut-location');
  const value = await askForFile();
  if (value != null) {
    iutLocationNode.value = value;
    doMotionDeblur(value);
  }
}

const setupEvents = () => {
  document.getElementById('iut-location-search').addEventListener('click', iutLocationSearchButtonClicked);
}