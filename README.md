# django-tasks
Simple to-do list app in Django for technical test.

## Host

The service is deployed and live thanks to Render. You can check it out here: https://django-tasks-4plq.onrender.com

The website may take around half a minute to load at first, because Render puts unused services down, so using this website after several minutes of inactivity causes it to put up the server fresh again.

## Manual setup

Clone the repository and open it in the terminal. Ensure you have `Python 3` installed and use a dedicated virtual environment, then run the following commands in order:

```bash
pip install -r requirements.txt;
cd todolist;
python manage.py makemigrations;
python manage.py migrate;
python manage.py collectstatic;
python manage.py runserver;
```

Then go to http://127.0.0.1:8000/

## Endpoint explanation

- "/" (GET): basic index homepage
- "/tasks" (GET): displays available tasks
- "/tasks/add"
    - POST: add a task to the database
    - GET: displays the add task form
- "/tasks/edit/<int>" (POST): change completed bool status of a task given its id
- "/tasks/delete/<int>" (POST): remove a task given its id
