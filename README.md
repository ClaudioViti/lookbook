# lookbook (multi-user version, no longer developed)

It's a shoes lookbook web app based on Django framework.
This app allows offers an inventory system to manage shoes items, with a specific detal fields.

----------------
First Installation guide:

sudo apt-get install python
sudo pip install django
rename settings.sample.py located in lookbook/ in settings.py
-----------------

to start the server run the following command: python manage.py runserver 0.0.0.0:8000

when an edit is made, the following commands are needed:

  python manage.py makemigrations
  
and
  
  python manage.py migrate
  
NOTE1: if "migrate" goes wrong, you can try deleting last migration .py file placed in shoes/migrations/

NOTE2: an edit to templates (.html) doesn't need to run the commands upon.

admin credentials: user: admin / password: testaccount

normal user credentials: user: user1 / password: testaccount
