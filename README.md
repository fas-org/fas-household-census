# fas-household-census
django app to collect data from households

prereqs:

python

django

To create login user:
```
python manage.py createsuperuser
```
To run migrations:
```
cd fas_questionnaire_site
python3 manage.py makemigrations fas_questionnaire
python3 managa.py migrate 
```

To run the app: 
```
python3 manage.py runserver 8080
```

http://localhost:8080/login/
