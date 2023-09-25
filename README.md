# Code Challenge Template
## Setup
- create and activate virtual environement
- install required packages: `pip install -r requirements.txt`

## Review by Problem
- solution for each problem is commited separately. Please check `commit` history
### Problem 1 - Data Modeling
- check data [model](weather/backend/models.py) in :file_folder:

### Problem 2 - Ingestion
- run `python manage.py makemigrations` to migrate model
- run `python manage.py migrate` to synchronize the database with the current model
- run `python manage.py ingest_weather_data` to ingest weather data into the database
- check [code](weather/backend/management/commands/ingest_weather_data.py) for data ingestion 

### Problem 3 - Data Analysis
- run  `python manage.py analyze_weather_data` to ingest weather data into the database
- check [code](weather/backend/management/commands/analyze_weather_data.py) for data analysis 

### Problem 4 - REST API
- run `python manage.py runserver`
- go to `http://127.0.0.1:8000/swagger` to check **swagger**
  - check `/api/weather` and `/api/weather/stats`
