# Django-Blog

## Prerequisites
* Users must have python3.x installed on their system.
* Users must have python3 virtualenv installed on their system.
* Install virtualenv using `sudo apt-get install python3-virtualenv`
* For git users installed Git using `sudo apt-get install git`

## Steps to run the project
* Clone the project using `git clone https://github.com/imrshu/Django-Blog.git` or just download the zip of project and extract it.
* Navigate to project directory and make an virtualenv using `python3 -m venv <virtual_env_name>`
* Activate the virtualenv using `source <virtual_env_name>/bin/activate`
* Now install dependencies using `pip install -r requirements.txt`
* Now `python manage.py migrate`
* Now create a super user using `python manage.py createsuperuser`
* Migrate the models using `python manage.py makemigrations`
* Now again migrate `python manage.py migrate`
* Finally run server up by using `python manage.py runserver`

### Note
* For captcha to run properly users should have some libraries installed on their system
* Run this command `sudo apt-get -y install libz-dev libjpeg-dev libfreetype6-dev python-dev`
