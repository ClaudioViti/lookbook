# lookbook

It's a shoes lookbook web app based on Django framework.
This app allows offers an inventory system to manage shoes items, with a specific detal fields.

to start the server run the following command: python.exe manage.py runserver 0.0.0.0:8000

when an edit is made, the following commands are needed:

  python.exe manage.py makemigrations
  
and
  
  python.exe manage.py migrate
  
NOTE1: if "migrate" goes wrong, you can try deleting last migration .py file placed in shoes/migrations/

NOTE2: an edit to templates (.html) doesn't need to run the commands upon.
