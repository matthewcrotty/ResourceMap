# Installation
First install mysql
On mac, install homebrew 
Follow instructions on https://tecadmin.net/install-mysql-macos/
In terminal run "pip install -r requirements.txt" 

## Server

To run the Flask server, navigate to the Flask directory inside the project repo in a terminal. Enter the following command:

export FLASK_APP=flask_app.py
export FLASK_DEBUG=1
python -m flask run

Open a browser and enter http://localhost:5000 in the url bar.

## Database

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

