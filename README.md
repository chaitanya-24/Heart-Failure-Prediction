# Heart Failure Prediction

This project is a web application that uses machine learning to predict the presence of heart disease in the patient based on various clinical features. The project was created by **Chaitanya Sawant**, a student of **G N Khalsa College, Mumbai**.

## Motivation

Heart failure is a common and serious condition that affects millions of people worldwide. It occurs when the heart cannot pump enough blood to meet the body's needs. Heart failure can lead to various complications, such as stroke, kidney damage, and death. Therefore, it is important to identify the risk factors and symptoms of heart failure and provide timely and appropriate treatment to the patients.

Machine learning is a branch of artificial intelligence that enables computers to learn from data and make predictions. Machine learning can be applied to various domains, such as healthcare, education, finance, and more. Machine learning can help to analyze large and complex datasets, discover hidden patterns and insights, and provide accurate and reliable predictions.

The aim of this project is to use machine learning to predict the presence of heart disease in the patient based on various clinical features. The project can help to provide a quick and easy way for users to assess their risk of heart failure, and to seek medical advice if needed.

## Features

The project has the following features:

- A web interface that allows users to enter their values for clinical features, such as age, sex, blood pressure, and more.
- A machine learning model that uses the user's input to predict the presence of heart disease, and displays the result on the web interface.
- A data preprocessing pipeline that transforms the raw data into a suitable format for the machine learning model.
- A dataset that contains records of patients with heart failure, along with their 12 clinical features and their survival status.

## Installation

To run the project locally, you need to have the following requirements:

- Python 3.7 or higher
- Flask 2.0.1 or higher
- Scikit-learn 0.24.2 or higher
- Pandas 1.3.2 or higher
- Numpy 1.21.2 or higher

You can install the required packages using the following command:

```pip install -r requirements.txt```

To run the project, you need to clone the GitHub repository using the following command:

```git clone https://github.com/chaitanya-24/Heart-Failure-Prediction.git```

Then, you need to navigate to the project directory and run the following command:

```python app.py```

The project will run on your local host at http://127.0.0.1:5000/

## Usage

To use the project, you need to follow these steps:

- Open the web interface at http://127.0.0.1:5000/
- Enter your values for the clinical features in the corresponding fields. The values should be within the specified ranges.
- Click on the "Result" button to submit your input and get the prediction result.
- The prediction result will show the presence of heart disease in the patient, it simply gives a message if heart disease is predicted or not.
- You can change your input values and click on the "Result" button again to get a new prediction result.

