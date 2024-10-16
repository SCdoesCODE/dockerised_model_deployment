# Use the official Python image as a base
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /predict_obesity_app

# Copy requirements file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]