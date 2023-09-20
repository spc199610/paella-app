This demo requires to have minikube and docker installed, also requires to start docker service before deployment.

To deploy paella-app use:
make deploy
    Starts minikube and builds the docker image used in this flask app.
    Deploys the application using minikube creating a 2 replica pods deployment and a nodeport type service, 
    for testing purposes it creates a port forwarding to receive inbound requests.

To destroy paella-app use:
make destroy
    Cleans up the resources deployed and stops minikube.

To test paella-app use:
make test
    Sends a POST request containing the example input json file in its body using curl.
    You can check your response with the output example provided in file "output_example.json".


