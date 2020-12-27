# Data-Representation-and-Querying-Project

![MotorCity](/staticpages/Images/Logo.PNG)
## Scope
To create an App Server that connects to a database and allows for CRUD opreations to be completed on the database. This app server should have a web interface to allow for user control.
[See here for instructions](project.pdf)

## Setup and run the project
1. Contained in the main folder are the SQL initialisation files for the "vehicles" database used in this project
2. Run createDatabase.py to initialise the "vehicles" database
3. Run createTable.py to initialise the starting tables of "cars" and suppliers" in the database. These tables are liinked on the SupplierID in each table
4. dbconfig.py contains the details of how to connect to the local MYSQL used during the development of this program. To connect to MYSQL on another PC, please edit the user and password to allow access to this. This dbconfig.py file has not been saved to Github, so a dbconfigTemplate.py file is also included to be copied and use for this purpose.
5. requirements.txt containes the packages used to successfully run this project. Please ensure these packes are all installed locally when testing.
6. From the main folder, run ".\venv\Scripts\activate.bat" to activate tha virtual environment
7. Use the command "set FLASK_APP=server" followed by "flask run" to start the Flask server
8. In the browser window, typing "http://127.0.0.1:5000" will bring up the homw page of the "MotorCity" API, connect to the database and display the initial cars and related suppliers in the database
9. Navigate to the Sales, Admin and Contact pages to perform the necessary CRUD operations on cars and suppliers tables.  