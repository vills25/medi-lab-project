### Project Medi Center

# Check python is installed or not
>>> python --version

# setup your project in local
>>>git clone https://github.com/vills25/medi-lab-project.git

# change your dir and go to "medi-lab-project"
>>>cd medi-lab-project

# Base dir:
medi-lab-project>

--------------------------------------------------------
# Create virtual environment
>>>python -m venv [testvenv]

# activate virtual environment
>>>[testvenv]\Scripts\activate

# deactivate virtual environment [optional]
>>>[testvenv]\Scripts\deactivate

([testvenv]) ...\medi-lab-project>
---------------------------
# check installed libraris and packages
>>>pip freeze/pip list
Package    Version
---------- -------
pip        23.3.1
setuptools 65.5.0

# create requirements.txt file
>>>type nul > requirements.txt

# Now, install/uninstall django 
>>> pip install/uninstall [lib/package name]
>>> pip install/uninstall django

# add your libraries and package list into the requirements.txt file
>>> pip freeze > requirements.txt

# create django project
>>> django-admin startproject [lab] .

# migrate your table into database
>>> python manage.py migrate

# create super user(Admin account)
>>> python manage.py createsuperuser
Username (leave blank to use 'admin'): admin
Email address: jgjs
Error: Enter a valid email address.
Email address: admin@gmail.com
Password:
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

# run your django-project in local server
>>> python manage.py runserver [port-number] + 8000

# create django application
>>> python manage.py startapp [master] 
- add in [project]>setting.py>[INSTALLED_APPS]

# Create model
>>> python manage.py makemigrations

---------------------------- Project plan ----------------------

Admin :
    Staff - Registration
Staff :
    Login - staff_id, password
