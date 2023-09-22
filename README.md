# Code Challenge Template
## Setup
- Create and activate virtual environement
- install required packages: `pip install -r requirements.txt`

## Review by Problem
- Solution for each problem is commited separately. Please check `commit` histroy
### Prblem 1 - Data Modeling
- check data model :folder in :file_folder:` weather/backend/models.py`

### Problem 2 - Ingestion
- run `python manage.py makemigrations` to migrate model
- run `python manage.py migrate` to synchronize the database with the current model
- run `python manage.py ingest_weather_data` to ingest weather data into the database

### Problem 3 - Data Analysis
- run run `python manage.py analyze_weather_data` to ingest weather data into the database

### Problem 4 - REST API
- run `python manage.py runserver`
- enter `http://127.0.0.1:8000/api/weather/?station_id=<station_id>&date=<date>` to check api/weather 
- enter `http://127.0.0.1:8000/api/weather/stats/?station_id=<station_id>&year=<year>` to check api/weather/stats
