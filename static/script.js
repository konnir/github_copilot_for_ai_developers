document.getElementById('analyze-button').addEventListener('click', async () => {
    const sentence = document.getElementById('sentence-input').value;

    // const response = await fetch(`http://${window.location.hostname}:8080/predict`, {
    // const response = await fetch('/predict', {
    // Automatically use the current protocol (HTTPS)
    const response = await fetch(`/predict`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ sentence: sentence })
    });
    const data = await response.json();
    const resultTextArray = data;

    // Extract the string from the array
    const resultText = resultTextArray[0];

    const resultImage = document.getElementById('result-image');
    const resultTextElement = document.getElementById('result-text');

    // Update the text content of the result-text element
    resultTextElement.textContent = resultText;
    console.log(resultText);

    // Update the src attribute of the result-image element based on the resultText
    switch (resultText) {
        case 'Anxiety':
            resultImage.src = '/images/anxiety.webp';
            break;
        case 'Normal':
            resultImage.src = '/images/normal.webp';
            break;
        case 'Depression':
            resultImage.src = '/images/depression.webp';
            break;
        case 'Suicidal':
            resultImage.src = '/images/suicidal.webp';
            break;
        case 'Bipolar':
            resultImage.src = '/images/bipolar.webp';
            break;
        default:
            console.error('Unknown result:', resultText);
            resultImage.src = '/images/logo.webp';
            break;
    }
});