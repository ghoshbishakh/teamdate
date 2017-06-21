runlocal:
	python manage.py runserver --settings=teamdate.settings.local

test:
	python manage.py test --settings=teamdate.settings.local

migrate:
	python manage.py migrate --settings=teamdate.settings.local

migrations:
	python manage.py makemigrations --settings=teamdate.settings.local
