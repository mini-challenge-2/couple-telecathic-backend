# Use the official Python base image
FROM python:3.10.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /app

# Expose the port on which the FastAPI application will run
EXPOSE 8000

# Run the FastAPI application using Uvicorn
CMD ["fastapi", "run"]