# Animal-Shelter-Database-Management-Application

## About the Project/Project Title
This application helps the user access and search a database of the animals at CS 340 Austin Animal Center (AAC). The user would ask Grazioso Salvare, the project requester, to create a dashboard and use it to search for animals using a filter. This project also gives the user access to charts, user interaction, and geolocation mapping for locating and using animals for search and rescue.

## Motivation
This project aims to give Python applications a reusable and effective means of interacting with MongoDB databases. By encapsulating CRUD operations within a Python class, developers can quickly incorporate MongoDB functionality into their projects without writing repetitive database interaction code.

## Tools
*	Python
*	MongoDB

## Why Python and MongoDB?
*	Python:
    *	Simplicity: Python's straightforward syntax and readability make it ideal for rapid development and maintenance.
    *	Rich Ecosystem: Python offers extensive libraries and frameworks for various tasks, facilitating seamless integration with other tools.
    *	Community Support: Python has a large and active community that provides resources, tutorials, and packages.
*	MongoDB:
    *	Flexible Data Model: MongoDB's document-based approach allows for easy handling of unstructured data, which is beneficial for managing diverse animal records.
    *	Scalability: MongoDB is designed to scale horizontally, accommodating growing data needs.
    *	Python Integration (pymongo): MongoDB's official Python driver (pymongo) provides a Pythonic interface for interacting with MongoDB, simplifying database operations.

## Motivation for Using Dash
Dash, the tool used to build the dashboard, was desirable due to its dynamic nature. Dash is a react JavaScript-based tool that provides an incredibly responsive framework. Dash involves HTML Dash tags that control outputs to segments. Then, updates to any of the target inputs specified in the app callbacks process are made based on instructions programmed in the Python module.
Getting Started

## Prerequisites
Make sure you have the following installed:
*	Python: Install Python (3.12 or higher) on your machine. Download from Python.org.
*	MongoDB: Install MongoDB on your machine. For installation guidelines, you can go to the MongoDB Download Center.
*	Jupyter Notebooks: You can install Jupyter Notebooks. Learn more about Jupyter Notebooks jupyter.org/install 
*	Plotly: Install Plotly. To get more information about Plotly, visit  plotly.com/python/getting-started/ 
*	Dash: You can install Dash. To explore Dash further, visit dash.plotly.com/installation 
*	Pandas: Install Pandas. For more details about Pandas, visit pandas.pydata.org/pandas-docs/stable/getting_started/install.html 

## Installation
### 1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/<your-username>/Animal-Shelter-Database-Management-Application.git
  ```
### 2. Import Data
Use the mongoimport command to import the CSV file aac_shelter_outcome.csv into MongoDB.

### 3. User Authentication Setup
Create user credentials and set up authentication for MongoDB.

### 4. Install the required Python packages 

## Usage
### MongoDB Import Execution
![MongoDB Import Execution](https://github.com/user-attachments/assets/e1f9b934-60e6-48c0-825a-7be948ab7a05)

### User Authentication Execution
![User Authentication Execution](https://github.com/user-attachments/assets/4209a988-8a3b-4f52-a0ae-98bc9064aff2)

### Create Method
* Description: Adds a document to the designated MongoDB collection and database.
*	Input: Accepts a set of key-value pairs that are compatible with the insert API call of the MongoDB driver.
*	Return: If the insert operation is successful, it returns True; if not, it returns False
![Create Method](https://github.com/user-attachments/assets/97e8d2fd-4cc0-4804-9117-10592471eae7)

### Read Method
* Description: Requests documents from the designated MongoDB collection and database.
* Input: Takes key/value lookup pairs for use with the find API call for the MongoDB driver.
* Return: If the query is successful, MongoDB returns an empty list; otherwise, it returns a cursor containing the results.
![Read Method](https://github.com/user-attachments/assets/27d68993-615f-4653-b145-02b54cc783f9)

### Update Method
* Description: Searches and modifies documents within the designated MongoDB collection and database.
* Return: If successful, return the updated document in JSON format; if not, return an error message. 
![Update Method](https://github.com/user-attachments/assets/89f7f5bc-738b-48bb-b789-ae0b44a82487)

### Delete Method
* Description: Searches and deletes documents from the designated MongoDB collection and database.
* Input: Accepts key/value lookup pairs for use with the find API call for the MongoDB driver.
* Return: If successful, MongoDB returns the outcome in JSON format; if not, it returns an error message. 
![Delete Method](https://github.com/user-attachments/assets/4db2ff94-6b8f-44c0-9460-83fc93341e28)

### Code Example
The following code demonstrates how to use the AnimalShelter class to add, read, update, and delete animals in a shelter:
![Code Example](https://github.com/user-attachments/assets/03e108fe-3d3f-4aed-89a4-884caabb7a87)

#### Dash Platform:
 
   * #### Dashboard Widgets:
     ![Dash Platform](https://github.com/user-attachments/assets/11609108-f637-4b17-8833-cc4015fe553c)

   * #### Filter Buttons:
     ![Filter Buttons](https://github.com/user-attachments/assets/e494999f-946a-4994-840c-1b53a9ea5b2a)

   * #### Geolocation Map:
     ![Geolocation Map](https://github.com/user-attachments/assets/aac51378-e82a-4112-a54a-0fd8d131af42)

   * #### Data Table:
     ![Data Table](https://github.com/user-attachments/assets/8eaad808-8120-4cd6-8850-695bbbe0e19f)

   * #### Pie Chart:
     ![Pie Chart](https://github.com/user-attachments/assets/e892a84d-1b31-4036-a32d-f5c054d69a23)


## Tests
#### Argument (Null) with the create() method will raise an error due to using an invalid argument, demonstrating error handling. 
![Argument_Null](https://github.com/user-attachments/assets/522cc5aa-e923-4262-8122-6f9c71f7f949)

#### CRUD functionality test execution Screenshots
![CRUD functionality test execution 1](https://github.com/user-attachments/assets/9fad39e6-b99a-488c-a1d3-1b4882c94bb1)
![CRUD functionality test execution 2](https://github.com/user-attachments/assets/f7a63305-bb5c-47c8-b30f-372d9234f224)
![CRUD functionality test execution 6](https://github.com/user-attachments/assets/6579de3f-496c-4379-ab90-a9b3d48af663)
![CRUD functionality test execution 5](https://github.com/user-attachments/assets/ac497600-2cb2-43fe-bef6-95a14e2085c7)
![CRUD functionality test execution 4](https://github.com/user-attachments/assets/0538ac66-e962-478b-9e91-829e8ca4c714)
![CRUD functionality test execution 3](https://github.com/user-attachments/assets/2a18c1bc-225b-4e65-aa12-6e543aad6c10)

 

### Challenges Encountered
* Data Import: Guaranteeing the integrity and correct formatting of imported data.
* User Authentication: Setting up MongoDB to safely require user authentication.
* Geolocation updates: The geolocation map didn’t update when switching filters.  Index selected rows by column names instead of indices
