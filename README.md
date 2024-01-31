# Backend Documentation for MindHive Project

## Overview
This project implements a backend API using Django REST Framework for serving data related to coffee shop outlets. The API provides functionality to retrieve names, addresses, and geographical coordinates of coffee shop outlets.

## Technologies
- Python: 3.8 - 3.11
- Django: 5.0.1
- Django REST Framework
- BeautifulSoup4 for web scraping
- Geopy for geocoding

## Part 1: Web Scraping and Database Storage
### Process
- Utilized BeautifulSoup4 to scrape outlet data from ZUS Coffee.
- Data includes outlet names and addresses.
- Pagination support implemented to navigate through multiple pages.
- Scraped data stored in a SQLite database using Django ORM.

### Limitations and Solutions
- Pagination Handling: Initially faced issues with correctly handling pagination. Solution implemented involves checking for a response status and the existence of data on subsequent pages.
- Data Duplication: To avoid duplicate entries in the database, a check was implemented to determine if an address already exists before storing.

## Part 2: Geocoding
### Process
- Geocoding was done using Geopy and OpenStreetMap's Nominatim service.
- Each outlet address was converted into geographical coordinates (latitude and longitude).

### Limitations and Solutions
- Incomplete Geocoding: Some addresses did not return coordinates. Implemented a fall-back mechanism to simplify addresses progressively for broader matches.
- Request Throttling: Implemented a sleep function to avoid hitting request limits of the geocoding service.

## Part 3: API Development
### Implementation
- Developed a RESTful API using Django REST Framework.
- API endpoints allow for retrieval of outlets data.
- Implemented ModelViewSet and a custom serializer for the Outlet model.

### Authentication
- API Key-based authentication implemented for secure access.
- Each API request requires a valid API key in the request header.

## Part 4: Frontend Development and Visualization (Not covered in this documentation)

## Deployment
- Deployed on PythonAnywhere (https://tahakh.pythonanywhere.com/api/).
- Process involved code upload, virtual environment setup, and WSGI configuration.

### Limitations and Solutions
- Geocoding Accuracy: Some addresses may not be precisely geocoded. We implemented a fallback mechanism to simplify addresses progressively for improved geocoding results.
- Scraping Dependence: The scraper's effectiveness depends on the structure of the ZUS Coffee website. Any significant changes to the website may require updates to the scraping logic.
- Authentication: API key authentication is used for simplicity. Consider more advanced authentication methods for production-grade applications.

## Security and Best Practices
- Token Authentication: REST Framework's Token Authentication is used for secure API access.
- CORS Policy: Configured to allow all origins for development purposes. This should be restricted in a production environment.

# Running the Project Locally

This section provides detailed instructions on how to set up and run the MindHive project in a local development environment.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python (version 3.8 - 3.11)
- pip (Python package installer)
- virtualenv (tool for creating isolated Python environments)

## Step 1: Clone the Repository
Clone the repository to your local machine:

git clone https://github.com/TahaKh99/mindhive.git cd mindhive

## Step 2: Set Up a Virtual Environment
Create a virtual environment in the project directory:

python -m venv venv

Activate the virtual environment:
- On Windows:

venv\Scripts\activate

- On macOS and Linux:

source venv/bin/activate

## Step 3: Install Dependencies
Install the required Python packages:

pip install -r requirements.txt

## Step 4: Database Setup
Perform database migrations to set up the database schema:

python manage.py migrate

## Step 5: Run the Development Server
Start the Django development server:

python manage.py runserver

The server will start at http://127.0.0.1:8000/. The API endpoints can be accessed at http://127.0.0.1:8000/api/outlets/.

## Step 6: API Authentication
To use the API with authentication:
1. Create a superuser account:

python manage.py createsuperuser

2. Follow the prompts to enter a username, email, and password.
3. Start the Django development server and log in to the admin panel at http://127.0.0.1:8000/admin/.
4. Navigate to the API Keys section and create a new API key.
5. Use this key in the Authorization header for authenticated API requests.

## Step 7: Running the Scripts
To run the scraping and geocoding scripts:
1. Activate the virtual environment and navigate to the project directory.
2. Execute the scripts:

python scraping.py python geocoding.py


## Note on Limitations
This local setup mimics the production environment but may have differences in performance and data handling. Ensure that CORS settings and debug mode are configured appropriately for production deployment.

## Conclusion
This documentation outlines the backend development process, challenges faced, and solutions implemented for the MindHive project. The project demonstrates capabilities in web scraping, geocoding, API development, and deployment using Django and associated technologies.
