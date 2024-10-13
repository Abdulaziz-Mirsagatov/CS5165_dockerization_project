# Use an official Python runtime as a base image
FROM python:3.9-alpine

WORKDIR /app

# Install the necessary packages
RUN pip install contractions

# Copy the current directory contents into the container at /app
COPY scripts.py /app/scripts.py
COPY /home/data/AlwaysRememberUsThisWay.txt /app/home/data/AlwaysRememberUsThisWay.txt
COPY /home/data/IF.txt /app/home/data/IF.txt
COPY /home/data/output /app/home/data/output

# Run the Python script
CMD ["python", "scripts.py"]
