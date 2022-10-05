from django.contrib import admin
from .models import RenteeUser
from .models import Listing
from .models import Category

# Register your models here.

# admin.site.register(RenteeUser)
# admin.site.register(Listing)

@admin.register(RenteeUser)
class RenteeUserAdmin(admin.ModelAdmin):
    list_display=('Name',)
    ordering=('Name',)
    search_fields=('Name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('Name',)
    ordering=('Name',)
    search_fields=('Name',)



@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display=('Name',)
    search_fields=('Name',)
    ordering=('Name',)