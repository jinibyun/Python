from django.contrib import admin
from first_app.models import AccessRecord, Topic, User, Webpage

# Register your models here.

# in order to register models to admin site
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User)