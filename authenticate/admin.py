from django.contrib import admin

from authenticate.models import CustomUser

admin.site.register(CustomUser)
