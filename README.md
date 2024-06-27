# Tarot Card App

## Accessing the Application
- URL: http://52.250.34.14/login
- Username: user
- Password: pass

## Azure Setup

1. Create a Resource Group
2. Create an Azure Kubernetes Service (AKS) Cluster
3. Connect to the AKS Cluster

## Container Registry Setup

1. Create an Azure Container Registry
2. Log in to the Azure Container Registry
3. Build and Push Docker Images
   - Ensure you have your Dockerfile for both the frontend and backend services
   - Navigate to the directory containing your Dockerfile and build the Docker images
4. Push the Docker images to Azure Container Registry

## Kubernetes Deployment

1. Create Kubernetes Secrets for PostgreSQL
2. Apply Kubernetes Manifests
   - Create a `deployment.yaml` file with the necessary configurations for your deployments and services
   - Apply the configurations
3. Verify Deployments and Services
   - Check the status of your pods and services to ensure everything is running correctly

## Application Configuration

1. Update Frontend Configuration
   - Ensure the frontend application is pointing to the correct backend service URL
   - Update the URL in your React components (e.g., `DrawCard.jsx`, `FortuneHistory.jsx`) to point to the backend-service external IP
2. Deploy Frontend Updates
   - Rebuild the frontend Docker image and push it to the Azure Container Registry
   - Apply the updated frontend deployment

## Monitoring and Maintenance

- Monitor Your Cluster
  - Use Azure Monitor and the Kubernetes dashboard to keep an eye on your deployments, pods, and services

## Local Development (Old)

```bash
docker-compose down
docker-compose up --build