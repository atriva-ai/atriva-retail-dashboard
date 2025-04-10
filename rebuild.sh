#!/bin/bash
CONTAINER_NAME="atriva-retail"
IMAGE_NAME="retail-dashboard"

echo "🛑 Stopping and removing old container..."
docker stop $CONTAINER_NAME 2>/dev/null && docker rm $CONTAINER_NAME 2>/dev/null

echo "🗑️  Removing old image..."
docker rmi $IMAGE_NAME 2>/dev/null

echo "🚀 Rebuilding the Docker image..."
docker build -t $IMAGE_NAME .

echo "🎯 Running the new container..."
docker run -d -p 5006:5006 --name $CONTAINER_NAME $IMAGE_NAME

echo "✅ Done!"


