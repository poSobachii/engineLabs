#!/bin/bash

echo "Starting the Angular Frontend..."
echo "==============================="

# Change to frontend directory
cd frontend

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Error: Node.js is not installed. Please install Node.js 16+ first."
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "Error: npm is not installed. Please install npm first."
    exit 1
fi

# Install Angular CLI if not present
if ! command -v ng &> /dev/null; then
    echo "Angular CLI not found. Installing globally..."
    npm install -g @angular/cli
fi

echo "Installing dependencies..."
npm install

echo "Starting Angular development server..."
echo "Frontend will be available at: http://localhost:4200"
echo "Make sure the backend is running on http://localhost:8080"
echo "Press Ctrl+C to stop the server"
echo ""

ng serve --host 0.0.0.0 --port 4200
