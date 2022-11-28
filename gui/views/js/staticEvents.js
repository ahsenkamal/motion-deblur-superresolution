const iutLocationSearch = async (event) => {
  const iutLocationNode = document.getElementById('iut-location');
  const value = await askForFile();
  if (value != null) {
    iutLocationNode.value = value;
  }
}

const generateVerilog = async (event) => {
  const projectLocation = document.getElementById('project-location').value;
  if (!projectLocation) {
    alert('Please provide project location');
    return;
  }

  const N = document.getElementById('n-bits').value;
  if (!N) {
    alert('Please provide the size of the adder');
    return;
  }

  eel.generateVerilog(projectLocation, currentAdder, Number.parseInt(N));
}

const setupEvents = () => {
  document.getElementById('iut-location-search').addEventListener('click', iutLocationSearch);
  document.getElementById('generate-button').addEventListener('click', generateVerilog);
}