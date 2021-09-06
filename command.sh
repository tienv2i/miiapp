#!/bin/bash
echo "Waiting for postgres..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 0.1
done
    echo "PostgreSQL started"

# if [[ ! -f "install.lock" ]];
# then
#     # python Pillow-8.2.0/setup.py --install
#     # pip install ./cached/Pillow-8.2.0.tar.gz
#     # pip install ./cached/Django-3.2.4-py3-none-any.whl
#     pip install -r ./requirements.txt
#     touch install.lock
# fi


python manage.py makemigrations
python manage.py migrate


if [[ "$DEBUG" == "True" ]];
then
    python manage.py runserver 0.0.0.0:8000
else
    gunicorn --bind :8000 miiapp.wsgi:application
fi


