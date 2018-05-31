# django-mvc
A project to learn the Django framework. . The goal of this project is to use all the capabilities of this framework to facilitate work in the future (this will help to increase the speed of programming in future projects). If you need to design a document in the future, I'll update it in this section.

for create new Project in Djnago first open terminal or cmd and write :
```
$ django-admin.py startproject myname
```

for run the server write this command . 5000 is port :
```
$ python manage.py runserver 5000
```
for create ```models.py``` and ```tests.py``` and ```views.py``` and ...
```
$ python manage.py startapp myname_api
```

if you migrate the model(DB) write this command :
```
$ python manage.py makemigrations
```

for create the tables in the database:
```
$ python manage.py migrate
```
and if you add model in models should to write 2 top command again.

for open shell project:
```
$ python manage.py shell
```

for create a user <b>admin site</b> :
```
$ python manage.py createsuperuser
```
