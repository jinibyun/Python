Class Base view (CBV) and templateview

all things for project and app should be setup (settings.py, urls.py ...) in advance.


1. views.py
	1. to see how it is changed.
		views.py > from django.views.generic import View
		
		urls.py > as_view()
	
		we need class CBView(View):
		
	2. compare function based view and class base view
		
	
	3. then, class based templateview
		1. IndexView section > get_context_data method
	    2. urls.py > as_view()
		
	4. ListView, DetailView (based on template view)
		1. models.py (create a model) > school and student class
		2. admin.py > register two classes
		3. python manage.py makemigrations
		4. python manage.py migrate
		5. python manage.py createsuperuser
		6. http://localhost:8000/admin/ and access to it and some of values using this admin panel for student and class
		
		(The following is an optional but good exercise for app extensibility)
		7. create templates/basic_app folder under basic_app 
		8. Then create html templage files under newly created folder (templates/basic_app)
		9. views.py > class SchoolListView and class SchoolDetailView
		10. templates > basic_app > base.html : look at navigation part
		11. http://localhost:8000/basic_app/list/ and check it out basic_app/templates/basic_app/school_list.html
		12. http://localhost:8000/basic_app/list/2/ and check it out basic_app/templates/basic_app/school_details.html
			check def get_absolute_url(self): in models.py
			
2. CRUD
	1. 	we need CreateView, UpdateView, DeleteView in views.py
		1. SchoolCreateView and school_form.html
			get_absolute_url in model is also neccessary
		2. SchoolUpdateView  and school_detail.html and urls.py
		3. SchoolDeleteView and school_confirm_delete.html and urls.py
			test: http://localhost:8000/basic_app/delete/3/
		
		