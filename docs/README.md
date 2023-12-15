# TheCough

## Description
A simple tool for teachers to count coughs in a classroom and send data to a server for analysis.

## Installation

### Mobile App
- Install Python and Kivy.
- Run `python mobile_app/main.py` to start the app.

### Backend Server
- Install Flask.
- Run `python server/app.py` to start the server.

### Database
- Run `python database/init_db.py` to initialize the database.

## Usage
- Tap the 'Count Cough' button to increment the cough count.
- Cough counts are automatically sent to the server.

## API Endpoints
- POST /cough: Receive cough data.
- GET /report: Generate and retrieve a report.
