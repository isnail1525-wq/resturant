from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'address')
    list_display_links = ('name',)   
    search_fields = ('name', 'email', 'phone')
