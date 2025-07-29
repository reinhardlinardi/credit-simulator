# Use an official Python runtime as a base image
FROM python:3.10-slim

# Copy app files
COPY . .

# Run the app
CMD ["python", "main.py"]
