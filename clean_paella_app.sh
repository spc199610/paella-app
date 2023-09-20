#!/bin/bash

# Cleaning deployed resources
kubectl delete deployment paella-app-deployment
kubectl delete svc paella-app-service

# Stop minikube
minikube stop
