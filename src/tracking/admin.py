from django.contrib import admin
from tracking.models import Projects, Contributor, Issues, Comments
# Register your models here.

admin.site.register(Projects)

admin.site.register(Contributor)

admin.site.register(Issues)

admin.site.register(Comments)
