from django.contrib import admin

# Register your models here.
from series.models import Language, Movie

admin.site.register(Language)
admin.site.register(Movie)
