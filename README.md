# Temperature Feed

# Description
This Django project provides a GraphQL API for monitoring and retrieving temperature readings. The application uses Graphene-Django to define and expose GraphQL queries for current temperature data and historical temperature statistics within specified time ranges.

# Features
- Current Temperature Query: Fetch the most recent temperature reading.
- Temperature Statistics Query: Fetch minimum and maximum temperatures over a specified date range.
- WebSocket Subscription: Real-time temperature updates (if applicable).

# Installation

## Prerequisites
- Python 3.7 or higher
- pip
- PostgreSQL

## Setup

1) Clone the Repository:
```
git clone https://github.com/Ashnayak/Temperature-Feed.git
cd Temperature-Feed
```

2) Install Required Packages:
```
pip install -r requirements.txt
```

3) Configure the Database:Edit the settings.py file to configure the database settings under the DATABASES section.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

4) Run Migrations:
```
python manage.py migrate
```

5) Start the Server:
```
python manage.py runserver
```

# Usage
Access the GraphQL interface through http://localhost:8000/graphql/ where you can execute queries like the following:

- Fetch Current Temperature:
```
query {
  currentTemperature {
    value
    timestamp
  }
}
```

- Fetch Temperature Statistics:
```
query {
  temperatureStatistics(after: "2024-01-01T00:00:00Z", before: "2024-01-02T00:00:00Z") {
    min
    max
  }
}
```

# Testing
Run the following command to execute automated tests:
```
pytest
```