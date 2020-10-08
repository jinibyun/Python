0. check it out very basic structure: setttings.py, urls.py ...
1. Template Tag
	1. first_app > urls.py: app_name = 'first_app'
		(NOTE: this must be setup)
	
	2. templates > first_app > look at four template html
		explain first about relative_url_template.html
		{% url %}
		
		1. test: http://localhost:8000/first_app/relative/
		2. exlain about relative url

	3. click on other page from "Link to other.html" section. 
		1. it will redirect to http://localhost:8000/first_app/other/
		2. explain about "template inheritance"
		
	4. Template filters (built-in) and customer filters
		1. first_app > index.html
		
		2. create templatetags folder (package) by manual  and create a file as below
			first_app\templatetags\my_extras.py
		(note) no registration in settings.py is needed.
