# Installation

## Server

Before proceeding, open a terminal. Navigate to the repository directory and enter the following command:

	pip install -r requirements.txt

Then navigate to the Flask subdirectory. Enter the following commands to launch the server on localhost:

	export FLASK_APP=flask_app.py
	export FLASK_DEBUG=1
	python -m flask run

Open a browser and enter http://localhost:5000 in the url bar.

## Database

In order to run this application, please install mysql on your machine if you have not already done

### Export 

To export mysql database to a .sql file (schema and data) in a terminal enter the following command (while in the top-level directory of the repository):

	mysqldump -u root -p dbname > db.sql

### Import

To import a mysql database from a .sql file open up a terminal and enter the following command to enter a mysql shell:

	mysql -u root -p

Then enter the following commands:

	create database Resources; //Only if it has not been created
	use Resources;
	source db.sql;

