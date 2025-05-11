
# superusername: Ishvari
# password: ishu@123



# Register your models here.
from django.contrib import admin
from .models import Bin

@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    list_display = ('location', 'area', 'status', 'waste_level')
    list_filter = ('area', 'status')
    search_fields = ('location', 'area')
