# UMass Roommate Finder Project

### How to set up the environment of this project:

#### Packages or libraries Requirements:
git -> 2.39.2

Python -> 3.9.6

django -> 3.2.19

Pillow -> 9.5.0

django-filter -> 23.2

bootstrap4 -> 0.1.0

#### Steps to create a virtual env:

* python -m venv myvenv

* Cd source/bin/activate (for mac) or myvenv\Scripts\activate (for Win)····

### Steps to set up the application:
* ensure you are in the directory that has the manage.py file
* Then execute the following commands to setup up the application: 
  * `python manage.py makemigrations`
  * `python manage.py migrate`
  * `python manage.py createsuperuser`
* In the above last command, since we are using a localhost, none of the data gets migrated, so, we need to create a user profile with unsername, user email, and password, which will be used later to log in our project website as an admin.

### How to launch the local server and direct to Admin login page:
* Execute the command `python manage.py runserver`
* Go to your web browser and type the following address into the search bar `127.0.0.1:8000/admin`, which will take you to the admin login page
* Enter the username and password you created previously to log in as an admin.
* Once log in to admin user page, you can lick on the "VIEW SITE" at the top right corner to be directed to the Home Page of your roommate-finder website.






