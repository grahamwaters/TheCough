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

## Setting Up the Environment

To set up the project environment, follow these steps:

1. Ensure you have Conda installed. If not, [install Miniconda](https://docs.conda.io/en/latest/miniconda.html) or Anaconda.

2. Navigate to the project directory in your terminal or command prompt.

3. Create the Conda environment using the `environment.yml` file:

    ```sh
    conda env create -f environment.yml
    ```


4. Once the environment is created, activate it:

    - Mac/Linux: `conda activate thecough`
    - Windows: `activate thecough`


5. Now, you can run the project components within this environment.


6. When you're done, deactivate the environment:

    - Mac/Linux: `conda deactivate`
    - Windows: `deactivate`