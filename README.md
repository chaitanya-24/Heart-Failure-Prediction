# Heart Failure Prediction

This project is a web application that uses machine learning to predict the presence of heart disease in the patient based on various clinical features.

## Motivation

Heart failure is a common and serious condition that affects millions of people worldwide. It occurs when the heart cannot pump enough blood to meet the body's needs. Heart failure can lead to various complications, such as stroke, kidney damage, and death. Therefore, it is important to identify the risk factors and symptoms of heart failure and provide timely and appropriate treatment to the patients.

Machine learning is a branch of artificial intelligence that enables computers to learn from data and make predictions. Machine learning can be applied to various domains, such as healthcare, education, finance, and more. Machine learning can help to analyze large and complex datasets, discover hidden patterns and insights, and provide accurate and reliable predictions.

This project aims to use machine learning to predict the presence of heart disease in the patient based on various clinical features. The project can help to provide a quick and easy way for users to assess their risk of heart failure, and to seek medical advice if needed.

## Features

The project has the following features:

- A web interface that allows users to enter their values for clinical features, such as age, sex, blood pressure, and more.
- A machine learning model that uses the user's input to predict the presence of heart disease, and displays the result on the web interface.
- A data preprocessing pipeline that transforms the raw data into a suitable format for the machine learning model.
- A dataset that contains records of patients with heart failure, along with their 12 clinical features and their survival status.


## Getting Started

To get a local copy up and running follow these simple steps:

1. Clone the repository
   ```sh
   git clone https://github.com/chaitanya-24/Heart-Failure-Prediction.git
   ```
2. Install the required libraries
   ```sh
   pip install -r requirements.txt
   ```
3. Run the main.py file
   ```sh
   python main.py
   ```
4. Open your browser and type http://127.0.0.1:5000/ in the address bar.

## Usage

The details of the patients (age, sex, blood pressure, serum creatinine, etc) are used to predict the likelihood of occurrence of death event due to heart failure. 

## Docker

The project can be run using Docker. To run the project using Docker, follow these steps:

1. Clone the repository
   ```sh
   git clone https://github.com/chaitanya-24/Heart-Failure-Prediction.git
   ```
2. Build the Docker image
   ```sh
   docker build -t heart-failure-prediction .
   ```
3. Run the Docker container
   ```sh
   docker run -p 5000:5000 heart-failure-prediction
   ```
4. Open your browser and type http://127.0.0.1:5000/ in the address bar.

## Github Actions

The project uses Github Actions for Continuous Integration. The workflow is triggered on every push to the main branch. The workflow runs the tests and builds the Docker image. If the tests pass and the Docker image is built successfully, the image is pushed to Docker Hub.

## Contributing

Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.


## Images
![h1](https://github.com/chaitanya-24/Heart-Failure-Prediction/assets/62403348/316f65cd-61d4-4bc7-ad8f-9dcffb1e8ffc)
![H2](https://github.com/chaitanya-24/Heart-Failure-Prediction/assets/62403348/ea992caf-3c14-4752-bd49-7a2f23174d84)
![H3](https://github.com/chaitanya-24/Heart-Failure-Prediction/assets/62403348/32b5945c-b3d5-4ba1-806a-480d193be55f)
