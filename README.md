# Flask_CRUD_Task
# Flask User Management API

This is a simple Flask-based API for managing user data with a MongoDB backend. It provides basic CRUD operations for user management.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- MongoDB installed and running on `localhost:27017` (You can modify the MongoDB URI in the `app.py` file if needed)
- Python virtual environment (optional but recommended)

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/yourusername/flask-user-management.git
   cd flask-user-management

   
2. Create a virtual environment (optional but recommended):
    python -m venv venv


3. Activate the virtual environment:
    venv\Scripts\activate


4. Install the required packages:
     pip install -r requirements.txt


5. Running the Application
    To run the Flask application, execute the following command:
       python app.py



#### The application will start and be accessible at http://localhost:5000.

API Endpoints
GET /get: Retrieve a list of all users.
POST /post: Create a new user.
PUT /update/<name>: Update an existing user by name.
DELETE /delete/<name>: Delete an existing user by name.
# Flask_CRUD_Task
