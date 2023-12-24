<h1> Search-for-handymen Website with Django </h1>


<h2>Project Overview</h2>

a web application designed to connect users with local handymen for various services. Users can search for handymen based on their location,
expertise. The platform aims to simplify the process of finding reliable handymen for home-related tasks.

<h2>Features</h2>
<hr/>

User Registration and Authentication:Users can register for an account, Authentication system to log in and log out.

Handyman Listings:Display a list of handymen available for  work, Include details such as name, skills, their location (wilaya) ...

Service Requests: Users can create service requests specifying the type of work they need. Include details such as description, location,phone nuumber.

Handyman Dashboard: Provide a dashboard for handymen to view and accept service requests, Handymen can update their profiles.

Admin Dashboard: An admin panel to manage user accounts, service requests, and handyman profiles,Only accessible to administrators.

Search and Filters:Implement a search for users to find specific handymen or services by location (wilaya).

<h2>Getting Started</h2>
<hr/>

Setup to run the application

first thing to do is to clone repository :

      $ git clone https://github.com/WebDevZakaria/deploysearch-for-handymen.git
 
      $ cd phonestore

Create a virtual environment to install dependencies in and activate it:

      $ virtualenv venv

      $ venv\Scripts\activate

      
Then install the dependencies:

      (venv) $ pip install -r requirements.txt
      
Note the (venv) should be in the front of the prompt. this indicate that the terminal session is in a virtual env

Once downloading the dependencies has finished you can start the server by running:

      (env) $ python manage.py runserver

And go to your browser and navigate to http://127.0.0.1:8000.



