# Portfolio_Python_App
Author: Charles Mudima

## Prerequisites
* Python 3.6.5
* Django 1.11.13

## Getting Started
To get started with this project, you need to do the following:
1. Clone the repo to your local machine
2. Install the requirements
3. Run the application

## Setup and installation
To run the application locally, one needs to have the following installed
1. Python 3.6 or later
2. pip
3. Virtual enviroment (optional)
4. Django 1.11 or later
5. A text editor of your choise (Recommend Visual Studio Code)

To run the application on your local machine, clone the repo by running `git clone

The implemented functionalities of this model include:
1. user Regstrationa and login
2. Add project information
3. view and edit thier profile 
4. view location using google API.

## User registration
A user will be directed to the home page where they will be able to register.
If they already have an account they can choose that option and sign in.
The information required upon registration is:
--> email
--> username
--> first name
--> last name
--> password
--> address
--> phone number 
--> location

## Add project information
When the user has successfully logged in a pop-up message will show on the screen. 
Once logged in the user will be at their dashboard where they can see their projects within the portfolio.
The current information displayed is dummy data. Essentially, what would be ideal would be to create a Projects model, where
all the projects are stored for each user. The current page outline is simplistic and aims to illustrate conceptualisation.

## View and edit profile
On the dashboard the user can go to their profile where they can see their personal information. Currently the editing functionality has not yet been implemented 

## View locations of all users
Lastly , on the dashboard the user can also view a map showing their current location. The intended functionality is to allow the user to see other users' location. The current markers are based on user current location and the other is hard coded.

## Limitations 
--> Editing profile
--> Viewing other user locations
--> Requires Google API to view the map 

## Built With
--> Time taken: 4 days
* [Django](https://www.djangoproject.com/) - The web framework used
* [Bootstrap](https://getbootstrap.com/) - The CSS framework used
* [JQuery](https://jquery.com/) - JavaScript library used
