# GitHub Copilot Generated Project Demo

This project is a demonstration of GitHub Copilot's capabilities, covering various aspects from exploring AI for mental health statements to model creation, setting up an HTTP server using FastAPI and Uvicorn, and creating a demo UI with HTML and JavaScript.

## Demo:
https://mental-549164777362.us-central1.run.app (allow few seconds to load)

## Overview

1. **Data Exploration**: Analyze mental health statements using AI.
2. **Model Creation**: Build and train models to predict mental health conditions.
3. **HTTP Server**: Implement an HTTP server using FastAPI and Uvicorn.
4. **Demo UI**: Develop a user interface with HTML and JavaScript to interact with the model.

## Dataset

The dataset used for this project can be found on Kaggle:
[data_set](https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health?resource=download)

## Features

- **Data Analysis**: Explore and preprocess the dataset.
- **Model Training**: Train machine learning models to classify mental health statements.
- **API Server**: Serve the model predictions through an HTTP API.
- **User Interface**: Provide a simple UI for users to input statements and get predictions.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the server:
    ```sh
    uvicorn main:app --reload
    ```

4. Open `index.html` in your browser to access the demo UI.

## Usage

1. Enter a mental health statement in the input box.
2. Click the "Analyze" button.
3. View the prediction and corresponding image below the input box.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
