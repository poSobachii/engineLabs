#!/bin/bash

echo "Starting the Java Spring Boot Backend..."
echo "======================================="

# Change to backend directory
cd backend

# Check if Maven is installed
if ! command -v mvn &> /dev/null; then
    echo "Error: Maven is not installed. Please install Maven first."
    exit 1
fi

# Check if Java is installed
if ! command -v java &> /dev/null; then
    echo "Error: Java is not installed. Please install Java 17+ first."
    exit 1
fi

echo "Installing dependencies and building..."
mvn clean install

echo "Starting Spring Boot application..."
echo "Backend will be available at: http://localhost:8080"
echo "H2 Database console: http://localhost:8080/h2-console"
echo "Press Ctrl+C to stop the server"
echo ""

mvn spring-boot:run
