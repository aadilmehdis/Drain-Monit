# Urban Drain Monitoring and Prediction

### Megathon 2019 | IIIT Hyderabad

## Idea
Monitor flow rate in urban storm water drainage pipes and predict the flow rate a few days ahead to provide adequate relief/management efforts for potentially critical locations.

## Components
- Django : Web App
- IoT device : Sensors for flow rate detection and transmitting data to central server

## Run the application

* `python sensor.py` to simulate real-time IoT device data transmission

* `python server.py` to host the D3 graphical visualization file (`data.json`)

* `python manage.py runserver` to run the web application

## Features

* Uses a simple ML model to predict future flow rate which can be extended to include other relevant parameters

* Visual data representation of per pipe flow rate and other pipe related details
