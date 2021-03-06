# flights
Simple web service that shows info about flights.  
Responds to GET /flights/*:id* and returns flight number, departure and arrival times in JSON format, where *:id* is id of the flight record in csv file.

## How to set up and run
1. Install required packages: 
 ```bash 
pip install -r requirements.txt
 ```
2. Create database: 
 ```bash 
python manage.py migrate
 ```
3. Populate database with data from csv file (location of test file is `files/flights.csv`):  
```bash
python manage.py load_flights <filename>
```
4. Run server: 
```bash
python manage.py runserver
```
## How to run tests
```bash
python manage.py test
```

