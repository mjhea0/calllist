# calllist
a networking and contact management web app

# call list

instructions for re-creating

### install

```sh
$ mkvirtualenv callist   
$ workon calllist  
$ pip install django
$ pip install ipython
$ django-admin.py startprject calllist
```
    
### test the install  

```sh 
$ python manage.py runserver
```
open browser to [http://localhost:8000](http://localhost:8000)

### add .gitgnore

### requirements.txt file

```sh
pip freeze > requirements.txt
```

### add to git

```sh
$ git init
$ git add .
$ git commit -m "initial commit"
```

### start the app

1. run
```sh 
$ python manage.py startapp tocall
```

2. add app to INSTALLED APPS in settings.py file 
3. add the data model to models.py 
4. check SQL then sync 
 
 ```sh
$ python manage.py sql tocall
$ python manage.py validate
$ python manage.py syncdb
```
