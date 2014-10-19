dropdb officeworks && createdb officeworks

rm -rf travel\migrations
rm -rf company\migrations

python manage.py makemigrations travel company
python manage.py migrate --noinput
python manage.py createsuperuser --username=ihabunek --email=ivan.habunek@gmail.com
python manage.py loaddata travel.json
