from django.contrib import admin
from .models import place
from .models import theme

admin.site.register(theme)

admin.site.register(place)
