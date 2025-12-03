from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Movie)

admin.site.register(models.Industry)

admin.site.register(models.Artist)

admin.site.register(models.Genre)

admin.site.register(models.languages)



