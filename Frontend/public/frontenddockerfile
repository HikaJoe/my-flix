# Use an official Nginx runtime as a base image
FROM nginx:latest

# Set the working directory to /usr/share/nginx/html
WORKDIR /usr/share/nginx/html

# Copy the contents of the local src directory to the working directory
COPY index.html .

# Expose port 80 to the outside world
EXPOSE 80
