0. How to setup virtual environment
	1. explain with presentation file
	
1. How to setup python django project

2. First Excercise
    1. config > settings.py > add 'first_app' into INSTALLED_APPS
    2. first_app > views.py > create index function
    3. config > urls.py > path('',views.index, name="index" ),
    4. test with browser

3. Add urls.py to first_app: urls.py

4. Change config > urls.py to point to first_app> urls.py file (make app as pluggable app)
    1. Test: http://localhost:8000/first_app/

5. django template
    1. create templates folder and first_app sub-folder where template files for first_app resides
    2. go to settings.py
        defined TEMPLATE_DIR and add it to TEMPLATES = [ ]
    3. add index.html to templates>first_app
	4. first_app>views.py>Index
	
6. static files (such as image, css and js etc)
	very similar to django template settings
	1. create static folder
	2. settings.py : look for STATIC_DIR. STATICFILES_DIRS needs to be added
	3. locate some jpg inside static\images
	4. locate some css file inside static\images
	5. go to index.html {% load static %} and {% static "css/mystyle.css" %}