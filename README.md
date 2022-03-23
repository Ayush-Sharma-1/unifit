# UniFit - University Guide

<h3>Context</h3>
UniFit is a django app that provides university recommendations for users based on their preferences. It will also work as a review system (along with it working as a  recommender system) such that the user will be allowed to leave a review for Universities and read other reviews. The application will provide precise information based on user input and user profile. This information will help the user identify which universities he/she/they have the best chance to get accepted in.
 

<h3>PreRequisite</h3>
1. python 3.7.2
2. Django 2.1.5
3. MySQL Instance 

<h3>Setup</h3>

The first step is to clone the repository
```bash
git clone https://github.com/Ayush-Sharma-1/unifit
cd uni_fit
```

Secondly, install the dependencies
```bash
python -m virtual venv
source venv/bin/activate
pip install -r requirements.txt
```

Setup DB
```bash
python manage.py makemigrations
python manage.py migrate
```

Add UniFit Data 
```bash
python population_script.py
```

To run the project
```bash
python manage.py runserver
```

## UniFit Walkthrough
###### Home Page 
Navigate to ```http://127.0.0.1:8000/```
Here the user will see the welcome page that introduces the site and directs them to register with a new account or to sign in using an existing account. 
Once the user is signed in, they will be able to select their prefereces such as  country and department of interest from a dropdown menu. This will filter out a set of results in a table that will display a list of universities according to their chosen selection. The list of universities will be ordered by rank.


###### University details
This view is available when you click on a university name from the table displayed on the home page. It contains detailed information on the specific university clicked on by the user. Here the user will be able to leave a review on the university and read reviews that have been submitted by other users. This page also uses a reddit API to display the mostpopular posts within the University's Reddit community. A list of reddit post titles are displayed, where a user can click on any title they wish to read, and it will direct them to a new tab with the post on reddit. This will allow them to read the replies and interact with the post. 

###### Profile
Navigate to ```http://127.0.0.1:8000/profile/```
This will display basic personal user information; also allows the user to enter their GPA(%) and the system will recommend a set of universities that match and align with their qualifications. User can also set a profile image.

###### Login
This option is available by clicking on the Login button on the index page or navigating to ```http://127.0.0.1:8000/auth/login/```.
User is able to login with their registered username and password. 

###### Sign up
This option is available by clicking on the Sign Up button on the index page or navigating to ```http://127.0.0.1:8000/auth/register/```.
User will be able to register entering their name, username, email, password, average GPA grade, their subject and set their preferences according to their county and department of interest.
