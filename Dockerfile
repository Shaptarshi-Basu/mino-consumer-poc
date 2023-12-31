# Use an official Python runtime as a parent image
FROM python:3.10.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 7000 for the Flask app
EXPOSE 7000

# Run app.py when the container launches
CMD ["python", "app.py"]
~                                