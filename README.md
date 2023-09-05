# Real Time Sign Language Detection Web App

This project is a real-time sign language detection web app built using React.js and TensorFlow.js. It allows users to use their webcam to perform sign language gestures, and the app will detect and display the corresponding sign language gesture in real time along with a probability score.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Data Collection and Labeling](#data-collection-and-labeling)
- [Fine-Tuning MobileNet](#fine-tuning-mobilenet)
- [Conversion to TensorFlow.js](#conversion-to-tensorflowjs)
- [Running the Web App](#running-the-web-app)
- [License](#license)

## Getting Started

### Prerequisites

Before running the app or following the steps below, make sure you have the following prerequisites installed:

- Node.js and npm: [Install Node.js](https://nodejs.org/)
- Python 3: [Install Python 3](https://www.python.org/downloads/)
- TensorFlow.js: Install it using `pip install tensorflowjs`

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/a-darsh/real-time-sign-language-detection
   
2. Navigate to the project directory:
   
  ```shell
  cd sig-detection-app
  ```
3.Install the required dependencies

  ```shell
  npm install
  ```

## Usage

The project consists of the following main components:

### Data Collection and Labeling

You can collect and label sign language gesture images using the provided Python script. The labeled images are stored in the `labeled_data` directory.

1. Navigate to the `data_collection` directory.
2. Modify the list of hand signs and the number of images per sign in the script.
3. Run the data collection script:

```shell
python collect_and_label_data.py
```
   
This script will capture images from your webcam, allow you to label them, and save them in the labeled_data directory.

### Fine-Tuning MobileNet
To fine-tune the MobileNet model:

Navigate to the fine_tuning directory.

Modify the script as needed, specifying paths and hyperparameters.

Run the fine-tuning script:

```shell
python fine_tune_mobilenet.py
```
This script loads the labeled data, fine-tunes the MobileNet model, and saves the model in the sign_language_detection_model directory.


### Conversion to TensorFlow.js
To convert the model to TensorFlow.js format:

Navigate to the conversion_to_tfjs directory.

Modify the paths in the script to point to your saved model.

Run the conversion script:
```shell
python convert_to_tfjs.py
```
This script converts the model to TensorFlow.js format and saves it in the tfjs_model directory.

### Running the Web App
Navigate to the sig-detection-app directory.

Start the React.js app:
```shell
npm run dev
```
This will start the development server, and you can access the web app in your browser at http://localhost:.


