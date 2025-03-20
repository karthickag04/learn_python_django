from django.contrib import admin
from .models import *

# Register your models here.


# class RegisterAdmin(admin.ModelAdmin):
#     # List the fields to display in the table
#     list_display = ('first_name', 'last_name', 'email', 'username', 'password')

#     # Optionally, you can add filters, search, or ordering
#     search_fields = ('first_name', 'last_name', 'email', 'username')
#     list_filter = ('last_name',)
#     ordering = ('first_name',)

# # Register the model with the custom admin class
# admin.site.register(Register, RegisterAdmin)

admin.site.register(login)
admin.site.register(Register)
