## URL Shortener Service

This project implements a URL shortener service using Flask, a lightweight web framework for Python. The service allows users to shorten long URLs into shorter ones and redirects users from the shortened URLs to the original ones.

## Features:

Shorten URLs: Users can submit long URLs to the service, which generates a unique shortened URL.
Redirect to Original URL: Shortened URLs redirect users to the original long URLs.
Dockerized: The application is containerized using Docker, making it easy to deploy and manage.

## Deployment:
The application has been deployed to a Minikube Kubernetes cluster for scalability and reliability.

## Technologies Used:
Python
Flask
Docker
Kubernetes (Minikube)

## Usage:
Submit a long URL to /shorten endpoint to receive a shortened URL.
Access the shortened URL to be redirected to the original URL.

## Run Locally:
To run the application locally, follow these steps:

## Clone the repository.

Build the Docker image using the provided Dockerfile.
Run the Docker container.
Access the service at http://localhost:9090.

## Deployment to Minikube:
To deploy the application to Minikube, follow these steps:

Install Minikube and start the cluster.
Apply Kubernetes manifests provided in the repository to deploy the application.
Access the service using the Minikube IP address and the specified port.