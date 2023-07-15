

from django.contrib import admin

from .models import artist_sell, Category, Profile, artworks, Buy

# Register your models here.
admin.site.register( artist_sell)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(artworks)
admin.site.register(Buy)

