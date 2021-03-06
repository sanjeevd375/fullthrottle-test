# fullthrottle-test
Sample django application with users and their respective activity.

### Codebase Setup

Step 1. Create Virtualenv and activate it.

      pip install virtualenv
      virtualenv venv
      . venv/bin/activate
Step 2. Clone the public git repository. Use the command below in terminal.

      git clone https://github.com/sanjeevd375/fullthrottle-test.git
Step 3. Install Requirements

      pip install -r requirements.txt
      
### MySQL Database Initialization

Run the below commands in mysql terminal to create database.

    CREATE DATABASE fullthrottle;
    GRANT ALL PRIVILEGES ON fullthrottle.* TO 'root'@'localhost';
    FLUSH PRIVILEGES;

Once database created modify the below configurations in "fullthrottle/settings.py" file.

      DATABASES = {
          'default':{
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'fullthrottle',
              'USER': 'root', 
              'PASSWORD': '<mysql-database password>',
              'HOST': 'localhost',
              'PORT': ''
          }
      }

### Migrate database, Dump sampledata and Start Server

Run the below command to initialize and start server.

    python manage.py makemigrations
    python manage.py migrate
    python manage.py loaddata sampledata.json
    python manage.py runserver
    
### Frontend View
Copy the url in browser to get list of user activity.

     http://localhost:8000/user/activity/

![Screenshot](frontend1.png)
![Screenshot](frontend2.png)

