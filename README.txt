# Flight Price Prediction Website

Welcome to the Flight Price Prediction website! This project aims to predict flight prices using a machine learning model. The website provides an interface for users to enter flight details and get price predictions.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Accurate Predictions**: Provides highly accurate flight price predictions to help users save money.
- **User-Friendly Interface**: Easy-to-use interface for entering flight details and receiving predictions.
- **Contact Form**: Users can contact us for inquiries or support.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/flight-price-prediction.git
    ```

2. Navigate to the project directory:

    ```bash
    cd flight-price-prediction
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - For Windows:

      ```bash
      venv\Scripts\activate
      ```

    - For macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Make sure the `flight_price_predictor.pkl` model file is in the project directory.

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Use the website to enter flight details and get price predictions.

## Directory Structure

```plaintext
flight_price_prediction/
├── app.py
├── model.py
├── flight_price_predictor.pkl
├── requirements.txt
├── static/
│   └── styles.css
└── templates/
    ├── index.html
    ├── predict.html
    ├── results.html
    ├── contact.html
    └── layout.html
