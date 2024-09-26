document.getElementById('testButton').addEventListener('click', async () => {
    const response = await fetch('/test');
    const data = await response.json();
    document.getElementById('inputText').value = data.line;
});

document.getElementById('predictButton').addEventListener('click', async () => {
    const text = document.getElementById('inputText').value;
    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    });
    const data = await response.json();
    document.getElementById('result').innerText = `Prediction: ${data.classification}`;
    setIcon(data.classification);
});

function setIcon(prediction) {
    const iconDiv = document.getElementById('icon');
    let icon = '';
    switch (prediction) {
        case 'Anxiety':
            icon = '😟';
            break;
        case 'Bipolar':
            icon = '😵';
            break;
        case 'Depression':
            icon = '😞';
            break;
        case 'Normal':
            icon = '😊';
            break;
        case 'Personality disorder':
            icon = '😕';
            break;
        case 'Stress':
            icon = '😫';
            break;
        case 'Suicidal':
            icon = '😢';
            break;
        default:
            icon = '';
    }
    iconDiv.innerText = icon;
}