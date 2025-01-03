# lookbook (multi-user version, currently developed)

It's a shoes virtual inventory web app based on Django framework.
This app allows offers an inventory system to manage shoes items, with a specific detailed fields.


First Installation guide:

sudo apt-get install python3 python3-venv python3-pip

move to home user directory and execute the following commands:

to create a virtualenv:
  
  python3 -m venv lookbook-venv

to activate a virtualenv:
  
  . lookbook-venv/bin/activate      (remember to exectute this command everytime you start the terminal)

pip install -r requirements.txt

clone the lookbook project in a different directory than the virtualenv diretory.

To start the server run the following command: python manage.py runserver 0.0.0.0:8000

when an edit to models.py is made, the following commands are needed:

  python manage.py makemigrations
  
and
  
  python manage.py migrate
  
NOTE1: if "migrate" goes wrong, you can try deleting last migration .py file placed in shoes/migrations/

NOTE2: an edit to templates (.html) doesn't need to run the commands upon.

admin credentials: user: admin / password: testaccount

normal user credentials: user: user1 / password: testaccount
