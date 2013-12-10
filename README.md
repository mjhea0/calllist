# calllist
    $ mkvirtualenv callist
    $ workon calllist
    $ pip install django
    $ pip install ipython
    $ django-admin.py startprject calllist
    
test the install  
 
     $ python manage.py runserver
     ⌘ (tab)     # to browser 
     ⌘ T     # new tab
     localhost:8000   # should auto complete
add to git

    $ git init
    $ git add .
    $ git commit -m "initial commit"    
start the app
     
     $ python manage.py startapp tocall
     
 add app to INSTALLED APPS in settings.py file  
 add the data model to models.py  
 check SQL then sync 
 
     $ python manage.py sql tocall
     $ python manage.py validate
     $ python manage.py syncdb
