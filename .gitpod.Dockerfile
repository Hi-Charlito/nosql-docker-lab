FROM gitpod/workspace-full

# Install Docker inside the workspace
USER root
RUN apt update && apt install -y docker.io docker-compose python3-pip

