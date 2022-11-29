const setupAdderSelection = () => {
    const adderSelectNode = document.getElementById('adder-selection');
    adderSelectNode.addEventListener('change', (event) => {
        currentAdder = event.target.value;
    });
    adderNames.forEach(adder => {
        const option = document.createElement('option');
        option.innerText = adder;
        option.value = adder;
        adderSelectNode.appendChild(option);
    });
    adderSelectNode.value = currentAdder;
};