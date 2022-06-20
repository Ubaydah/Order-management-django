release: python manage.py makemigrations
release: python manage.py migrate

worker: celery -A orderSystem worker -l info -B

web: gunicorn orderSystem.wsgi --log-file -




