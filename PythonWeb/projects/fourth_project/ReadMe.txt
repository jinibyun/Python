0. Prestudy
	1. SHA (secure hash algorithm)
		ref: https://xorbin.com/tools/sha256-hash-calculator

(registration first)
	
	1. python manage.py migrate (NOTE: no django migrate)
	2. check database
	3. more advanced security algorithm
		pip install bcrypt
		pip install django[argon2] : probably already. But just want to make sure
	4. settings.py > add PASSWORD_HASHERS
		1. in order to use password_hash...
		2. It will be sued with AUTH_PASSWORD_VALIDATORS
		3. create media, static, and template folder and register in settings.py (which are related to login. It will be explained later)
		
		4. User Auth Model (Built-in)
			1. in order to use ImageField, "python -m pip install Pillow".
		4-1. Once created for model, do not forget to apply to DB: python manage.py makemigrations and python manage.py migrate
		
		5. create forms.py
		
		6. register UserProfileInfo model in models.py to admin.py
			
		7. look at template html file under templates>base_app
		8. modify config > urls.py
		9. add basic_app > urls.py
		10. (TEST)
			1. registration first. also double check with database once registration is successful.
			2. stop service and python manage.py createsuperuser
			3. http://localhost:8000/admin to access to admin. Confirm if User Profile Info exist
		
(then, login)
	1. create user_login on views.py	
	2. user_logout