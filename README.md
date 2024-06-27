# This is a tarot card app. 
## Accessing the Application
http://52.250.34.14/login
### Username: user
### Password: pass

# Azure Setup
## Create a Resource Group
## Create an Azure Kubernetes Service (AKS) Cluster
## Connect to the AKS Cluster

# Container Registry Setup
## Create an Azure Container Registry
## Log in to the Azure Container Registry
## Build and Push Docker Images
### Ensure you have your Dockerfile for both the frontend and backend services. Navigate to the directory containing your Dockerfile  and build the Docker images.
## Push the Docker images to Azure Container Registry.

# Kubernetes Deployment
## Create Kubernetes Secrets for PostgreSQL
## Apply Kubernetes Manifests
### Create a deployment.yaml file with the necessary configurations for your deployments and services. Then apply the configurations.
## Verify Deployments and Services
### Check the status of your pods and services to ensure everything is running correctly.

# Application Configuration
## Update Frontend Configuration
### Ensure the frontend application is pointing to the correct backend service URL. Update the URL in your React components (e.g., DrawCard.jsx, FortuneHistory.jsx) to point to the backend-service external IP.
## Deploy Frontend Updates
### Rebuild the frontend Docker image and push it to the Azure Container Registry.
### Apply the updated frontend deployment.

# Monitoring and Maintenance
## Monitor Your Cluster
### Use Azure Monitor and the Kubernetes dashboard to keep an eye on your deployments, pods, and services.



# local (old)
# docker-compose down
# docker-compose up --build