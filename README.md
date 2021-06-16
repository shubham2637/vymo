
<b>Assignment Problem Statement:</b><br>

A food delivery company wants to self onboard the restaurants.
Design a system that collects basic merchant details (restaurant name, contact name, Pincode,
location, website, phone number, average daily transactions).
Use API to connect frontend and database servers. You can either use SQL or NoSQL databases.
Users should be able to submit the form and if successfully submitted, see the status, failure
status otherwise



Getting Started
---------------
To get up and running, simply do the following:

    $ git clone git@github.com:shubham2637/vymo.git
    $ cd vymo

    # Install the requirements
    $ pip install -r requirements.txt



    # Perform database migrations if required
    $ python manage.py makemigrations
    $ python manage.py migrate
    
    # Start the server
    $ python manage.py runserver
    
    Open bowser at http://127.0.0.1:8000
    Admin Login : http://127.0.0.1:8000/admin
                username : admin 
                password : admin
    

    #for Rest APIs
    method                      URL                                   Discription
    GET                 http://127.0.0.1:8000/api/merchant       :  Lists all merchant
    POST                http://127.0.0.1:8000/api/merchant       :  Adds merchant
    GET,DELETE,PUT       http://127.0.0.1:8000/api/merchant/<pk> :  CRUD on merchant id

**NOTE**: I highly recommend creating a [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/). Python Virtual Environments allow developers to work in isolated sandboxes and to create separation between python packages installed via [pip](https://pypi.python.org/pypi/pip).
