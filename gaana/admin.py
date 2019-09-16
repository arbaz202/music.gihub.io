from django.contrib import admin
from .models import Album,Song,Profile,ShipPhoto
# Register your models here.
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Profile)
admin.site.register(ShipPhoto)
