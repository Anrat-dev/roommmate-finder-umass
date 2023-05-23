# UMass Roommate Finder Project

### How to set up the environment of this project:

#### Packages or libraries Requirements:
git -> 2.39.2

python -> 3.9.6

django -> 3.2.19

pillow -> 9.5.0

django-filter -> 23.2

bootstrap4 -> 0.1.0

bootstrap-form -> 3.4

django-widget-tweaks -> 1.4.12

#### Steps to create a virtual env:

* python -m venv myvenv

* Cd source/bin/activate (for mac) or myvenv\Scripts\activate (for Win)····

### Steps to set up the application:
* make sure you are at the root directory **roommmate-finder-umass/** that has the manage.py file
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


### How to run all the test cases：
* make sure you are at the root directory **roommmate-finder-umass/** that has the manage.py file
* run `python manage.py test register/tests` to run all the test cases for user registration verification.
* run `python manage.py test webappl/tests` to run all the test cases for user profile create/edit/update/delete, roommate search/filter, and connection request/accept related operations.

### Github username of each group member:
* Name : **Noah Dixon**

  Github username : noahdixon

* Name : **Anurati Bhosekar**

  Github username : Anrat_dev


* Name : **Sijia Hao**

  Github username : Scarlett-HS

* Name : **Dishank Deven Jhaveri**

  Github username : dishank19





