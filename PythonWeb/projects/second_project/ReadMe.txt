0. create new project and app at first

1. Before creating any model, confirm DATABASES section in settings.py

2. python manage.py migrate
   1. built-in database scripts will generates table
   2. confirm with DB Broswer for SQLite

3. Model creation basic
	1. Creating Model - start with models.py
		django model ref: https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types
	2. NOTE: the app must be registered in INSTALLED_APPS section in settings.py
	
	3. python manage.py makemigrations
		
	4. python manage.py migrate
	
	5. confirm with DB Broswer for SQLite
	
	6. python manage.py shell  (to interact database)
		e.g.
			>>> from first_app.models import Topic
			>>> print (Topic.objects.all())
			<QuerySet []>
			>>> t = Topic(top_name="Social Network")
			>>> t.save()
			>>> print (Topic.objects.all())
			<QuerySet [<Topic: Social Network>]>
			>>> quit()
	7. Another way to access DB via python: go to admin.py and register model
	8. python manage.py createsuperuser : to access admin on browser
	9. python manage.py runserver and access http://localhost:8000/admin
		checkout Topics or whatever...model. to add, edit, delete..etc
4. Populating Script
	1. "pip install Faker" under virtual environment
		populate with fake data. checkout documentation (https://faker.readthedocs.io/en/master/providers/faker.providers.company.html)
	2. create populate_first_app.py	
	3. run: python populate_first_app.py
	4. python manage.py runserver > confirm http://localhost:8000/admin on browser
	
5. Model Template View (MTV paradigm)
	(NOTE) step
	1. first_app > views.py	(add models and query and pass "model" to "view")
	2. look at templates > first_app > index.html (careful about template syntax)
	3. make sure urls.py (two urls.py files)
	4. run server 
	
6. django form
	1. Form without Model
		1. create templates > first_app> form.page.html
		2. create first_app > forms.py
		3. define form_name_view function inside views.py
		4. change config > urls.py and first_app > urls.py
		5. review inject section of form.page.html
		6. simple test: submit button click and see..data
		7. Form Validation
			(skip) 1. how to render hidden tag and clean_botcatcher method is just a test
				(when testing hidden tag, insert some value in F12 developer tool)
				
			(built-in validation)
			2. from django.core import validators
			
			(custom validation)
			3. explain about check_for_z which is custom validator
			4. def clean(self)
	2. Form with Model Connected (ModelForm)
		
		1. first_app > add users.html
		2. models.py : add class User(models.Model): 
			(NOTE) once any new class is made on models.py, don't forget two things:
				python manage.py makemigrations
				python manage.py migrate
			(NOTE) in order to be maintained in admin site later, it should be registered in admin.py
		3. first_app > forms.py  add class named "NewUserForm"
		4. views.py : add def users(request):
		5. urls.py
		
	
	