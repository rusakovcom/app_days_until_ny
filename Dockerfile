# docker build -t app_days_until_ny .
# docker run -d --name app -p 80:5000 app_days_until_ny

# Use the official Python image from the Docker Hub
FROM python:alpine3.20

# Set the working directory in the container
WORKDIR /app

# Copy the requirements and app files into the container
COPY requirements.txt app.py ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "--log-level=debug", "--access-logfile", "-", "app:app"]
