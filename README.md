# Animal-Shelter-Database-Management-Application

## About the Project/Project Title
A database of the animals at CS 340 Austin Animal Center (AAC) can be accessed and searched by the user with the help of this application. The user would ask Grazioso Salvare, the project requester, to create a dashboard and use it to search for animals using a filter. This project also gives the user access to charts, user interaction, and geolocation mapping for the purpose of locating and using animals for search and rescue.

## Motivation
This project aims to give Python applications a reusable and effective means of interacting with MongoDB databases. Developers can quickly incorporate MongoDB functionality into their projects without writing repetitive database interaction code by encapsulating CRUD operations within a Python class.

## Tools
*	Python
*	MongoDB

## Why Python and MongoDB?
*	Python:
    *	Simplicity: Python's clear syntax and readability make it ideal for rapid development and maintenance.
    *	Rich Ecosystem: Python offers extensive libraries and frameworks for various tasks, facilitating seamless integration with other tools.
    *	Community Support: Python has a large and active community, providing resources, tutorials, and packages.
*	MongoDB:
    *	Flexible Data Model: MongoDB's document-based approach allows for easy handling of unstructured data, which is beneficial for managing diverse animal records.
    *	Scalability: MongoDB is designed to scale horizontally, accommodating growing data needs.
    *	Python Integration (pymongo): MongoDB's official Python driver (pymongo) provides a Pythonic interface for interacting with MongoDB, simplifying database operations.

## Motivation for Using Dash
Dash, as the tool used to build the dashboard, was desirable due to its dynamic nature. Dash is a react JavaScript based tool that provides an incredibly responsive framework. Dash involves html Dash tags that control outputs to segments. Then, updates to any of the target inputs specified in the app callbacks process based on instructions programmed in the Python module.
Getting Started

## Prerequisites
Make sure you have the following installed:
*	Python: Install Python (3.12 or higher) on your machine. Download from Python.org.
*	MongoDB: Install MongoDB on your machine. For installation guidelines, go to the MongoDB Download Center.
*	Jupyter Notebooks: You can install Jupyter Notebooks. Learn more about Jupyter Notebooks jupyter.org/install 
*	Plotly: Install Plotly. Get more information about Plotly vist  plotly.com/python/getting-started/ 
*	Dash: You can install Dash. Explore Dash further visit dash.plotly.com/installation 
*	Pandas: Install Pandas. For more details about Pandas, visit pandas.pydata.org/pandas-docs/stable/getting_started/install.html 

## Installation
### 1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/<your-username>/Animal-Shelter-Database-Management-Application.git
  ```
### 2. Import Data
Use mongoimport command to import csv file aac_shelter_outvome.csv into MongoDB.

### 3. User Authentication Setup
Create user credentials and set up authentication for MongoDB.

### 4. Install the required Python packages 

## Usage
### Create Method
* Description: Adds a document to the designated MongoDB collection and database.
*	Input: Accepts a set of key-value pairs that are compatible with the insert API call of the MongoDB driver.
*	Return: If the insert operation is successful, it returns True; if not, it returns False

### Read Method
•	Description: Requests documents from the designated MongoDB collection and database.
•	Input: Takes key/value lookup pairs for use with the find API call for the MongoDB driver.
•	Return: If the query is successful, MongoDB returns an empty list; otherwise, it returns a cursor containing the results.

### Update Method
•	Description: Searches and modifies documents within the designated MongoDB collection and database.
•	Return: If successful, returns the updated document in JSON format; if not, returns an error message. 

### Delete Method
•	Description: Searches and deletes documents from the designated MongoDB collection and database.
•	Input: Accepts key/value lookup pairs for use with the find API call for the MongoDB driver.
•	Return: If successful, MongoDB returns the outcome in JSON format; if not, it returns an error message. 

### Code Example
The following code demonstrates how to use the AnimalShelter class to add read, update, and delete animals in a shelter:

#### Dash Platform:
 
#### Dashboard Widgets:
#### Filter Buttons:
 
#### Geolocation Map:
 
#### Data Table:
 
#### Pie Chart:
 

### Tests
1.	Argument (Null) with the create() method will raise an error due to using an invalid argument, demonstrating error handling. 
 
CRUD functionality test execution Screenshots
 
 

### Challenges Encountered
•	Data Import: Guaranteeing the integrity and correct formatting of data that is imported.
•	User Authentication: Setting up MongoDB to safely require user authentication.
•	Geolocation updates: The geolocation map didn’t update when switching filters.  Index selected rows by column names instead of indices
