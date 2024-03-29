# django-tasks
Simple to-do list app in Django for technical test.

## Host

The service is deployed and live thanks to Render. You can check it out here: https://django-tasks-4plq.onrender.com

The website may take some seconds to load at first, because Render puts unused services down, so loading it causes it to put up the server fresh again.

## Manual setup

Clone the repository and open it in the terminal. Ensure you have `Python 3` installed, then run the following commands in order:

```bash
pip install -r requirements.txt;
cd todolist;
python manage.py makemigrations;
python manage.py migrate;
python manage.py runserver;
```

Then go to http://127.0.0.1:8000/
