# Dockerized Obesity Prediction App

This repository contains a simple web application designed to predict the health status of a person in terms of weight (e.g. obesity) based on certain input features. The machine learning model, which is trained using the XGBoost algorithm, is containerized using Docker for easy deployment and sharing.

## Project Structure

- **obesity_data.ipynb**: Contains the Jupyter notebook with the research, data analysis, model training, and testing processes. This notebook documents the steps taken to develop and evaluate the machine learning model used in the web app.
  
- **app.py**: The Flask web application that serves the model for prediction.
  
- **Dockerfile**: The configuration file for containerizing the web app using Docker.

## Getting Started

To run this project on your local machine, you will need to have [Docker Desktop](https://www.docker.com/products/docker-desktop) installed. Follow the steps below to build and run the application.

### 1. Clone the Repository

```bash
git clone git@github.com:SCdoesCODE/dockerised_model_deployment.git
cd dockerised_model_deployment 
```

### 2. Build the Docker Image

In the terminal, run the following command to build the Docker image for the application:

```bash
docker build -t predict_obesity_app .
```

### 3. Run the Docker Container

Once the image is built, you can run the container with the following command:

```bash
docker run -p 5001:5000 predict_obesity_app
```

### 4. Access the Web Application

The application will be available locally at: http://localhost:5001/predict. You can interact with the app to input features and receive predictions on a person’s health status.

## Model Information
The model used in this web app was trained using a dataset on obesity from Kaggle, and it predicts whether a person falls into categories such as obesity or normal weight based on their input data. The model was developed in Python using the XGBoost algorithm for its strong performance in classification tasks.

You can find the complete research, data exploration, and model evaluation in the *obesity_data.ipynb* notebook.

## Dependencies
- Flask: A lightweight web framework used to build the web application.
- XGBoost: The machine learning algorithm used for training the obesity prediction model.
- Docker: The platform used to containerize the web app for easy deployment.

To install additional dependencies, refer to the *requirements.txt* file 

