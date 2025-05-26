 This document outlines the steps to build, tag, and push Docker images specifically for the `linux/amd64` architecture.  This is important for ensuring compatibility when deploying to environments that require this architecture, such as some Azure services or specific on-premises servers.  We'll cover the `pgadmin` and `postgres` images as examples, as well as a general Dockerfile build process.
Example with pgadmin only the same goes for Postgres and fastapi images
## Prerequisites

*   **Docker:**  Ensure you have Docker installed and running on your system.
*   **Azure CLI (Optional):**  If you're pushing to Azure Container Registry (ACR), ensure you have the Azure CLI installed and are logged in to your Azure account.  (`az login`)
*   **Azure Container Registry (ACR):**  You need an existing Azure Container Registry to push your images to.  Replace `registryexp.azurecr.io` with your actual ACR name.
*  **Docker Buildx:** Make sure you have Docker Buildx installed and configured.  Buildx allows building multi-platform images.

## Building and Pushing images (AMD64)

Since `pgadmin` already has been specified in the docker-compose.yml file simply type for having amd64 images only


### 1. Pull the pgAdmin Image

This command pulls the latest `pgadmin4` image from Docker Hub, automatically selecting the `amd64` variant if available. Docker will handle architecture selection during the pull.

```bash
docker pull dpage/pgadmin4:9

docker tag dpage/pgadmin4:9 registryexp.azurecr.io/pgadmin:v5

docker push registryexp.azurecr.io/pgadmin:v5







