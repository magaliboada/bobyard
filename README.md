# Bobyard

Comment functionality. 

## Prerequisites

- Docker installed on your system

## Project Structure

- `backend/`: Django-based REST API and Postgres
- `frontend/`: Build with React and Chakra UI
- `Bobyard.postman_collection.json`: API documentation and testing collection

## Backend Structure

Notes: 
1. I am aware this structure might be more or less convenient depending on the company situation. I'm open to different ways of organizing the code and happy to adapt to the team's preferences.

2. About the tests: normally I would have written them, but since you mentioned you don’t usually do them, I preferred to spend that time polishing the frontend instead :)

- `domain/`: Contains the business logic and entities
- `application/`: Handles use cases 
- `infrastructure/`: Manages database and API


## Getting Started

1. Start the backend service:
```bash
docker-compose -f backend/docker-compose.yml up -d
```

2. Start the frontend service:
```bash
docker-compose -f frontend/docker-compose.yml up -d
```

## Accessing the Application

- Frontend: http://localhost:8080
- Backend API: http://localhost:3000

## Stopping the Services

To stop all services:
```bash
docker-compose -f backend/docker-compose.yml down
docker-compose -f frontend/docker-compose.yml down
```
