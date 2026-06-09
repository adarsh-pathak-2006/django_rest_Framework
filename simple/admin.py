from django.contrib import admin
from .models import database, info


admin.site.register(database)
admin.site.register(info)