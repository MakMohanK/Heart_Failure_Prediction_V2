# Heart Failure Prediction Using Random Forest

## Overview
This project involves the analysis and prediction of heart failure risk using a Random Forest machine learning model. The model is trained on customized data, including various patient health metrics, to predict the likelihood of heart failure. The goal is to provide a tool that can assist healthcare professionals in identifying high-risk patients.

## Table of Contents
Overview
Features
Project Structure
Installation
Usage
Dataset
Model Details
Evaluation
Results
Contributing
License
Features


## Data Preprocessing: 
Handles missing values, normalization, and feature engineering.
Model Training: Utilizes the Random Forest algorithm for classification.
Feature Importance: Identifies the most significant predictors of heart failure.
Prediction: Provides heart failure risk predictions for new patients.
Evaluation: Includes model evaluation metrics such as accuracy, precision, recall, and ROC-AUC.

## Project Structure
~~~python
heart-failure-prediction/
│
├── data/
│   └── heart_failure_custom_data.csv   # Customized dataset
├── model/
│   └── random_forest_model.pkl         # Trained Random Forest model
├── notebooks/
│   └── data_preprocessing.ipynb        # Data preprocessing steps
│   └── model_training.ipynb            # Model training and evaluation
├── static/
│   └── images/
│       └── example_image.jpg           # Example image for README
├── templates/
│   └── index.html                      # Flask HTML template
├── app.py                              # Flask application
├── requirements.txt                    # Python dependencies
├── README.md                           # Project README file
└── LICENSE                             # License file
~~~

## Installation
Clone the repository:
~~~python
git clone https://github.com/yourusername/heart-failure-prediction.git
~~~

## Navigate to the project directory:
~~~python
cd heart-failure-prediction
~~~
## Create a virtual environment:

~~~python
python -m venv venv
~~~
## Activate the virtual environment:

### On Windows:

~~~python
venv\Scripts\activate
~~~

### On macOS/Linux:
~~~python
source venv/bin/activate

~~~

## Install the dependencies:
~~~python
pip install -r requirements.txt
~~~

# Usage
## Run the Flask application:
~~~python
python app.py
~~~

Access the application:

Open your web browser and navigate to http://127.0.0.1:5000/.

## Upload Data & Predict:

Upload patient data and get predictions on the likelihood of heart failure.

## Dataset
The dataset used in this project is a customized collection of patient health metrics, including features like age, blood pressure, cholesterol levels, and more. It is stored in data/heart_failure_custom_data.csv.

## Model Details
The model is a Random Forest classifier trained to predict heart failure. The training process includes:

## Hyperparameter Tuning: 
Optimized for best performance.
Cross-Validation: Ensures model robustness.
Feature Importance: Highlights key predictors of heart failure.
Evaluation
The model is evaluated using various metrics:

## Accuracy: 
Measures the overall correctness of predictions.
Precision & Recall: Evaluates the balance between false positives and false negatives.
ROC-AUC Curve: Assesses the model’s discrimination ability.
Results
The Random Forest model achieved an accuracy of X% on the test data, with a precision of Y% and recall of Z%. The ROC-AUC score was W.