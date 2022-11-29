const saveButtonClicked = async (event) => {
  askAndSaveImage(document.getElementById('out').src);
}

const setupEvents = () => {
  document.getElementById('save-button').addEventListener('click', saveButtonClicked);
}