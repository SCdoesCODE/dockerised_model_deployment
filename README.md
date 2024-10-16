# dockerised_model_deployment

To run this repo you need to download the docker desktop application and open it

In the terminal run:
* docker build -t predict_obesity_app .
* docker run -p 5001:5000 predict_obesity_app

Access the application locally at: http://localhost:5001/predict

