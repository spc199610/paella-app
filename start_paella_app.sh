#!/bin/bash

# Start Minikube
minikube start

# Configure the Docker environment to use Minikube's Docker daemon
eval $(minikube docker-env)

# Build the Docker image
docker build -t paella-app .

# Apply the configuration files to Kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Wait until the pods are ready
kubectl wait --for=condition=Ready pod -l app=paella-app --timeout=300s

# Forward the service port
kubectl port-forward --address 0.0.0.0 -n default service/paella-app-service 30007:80

