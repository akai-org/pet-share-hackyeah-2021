from django.contrib import admin

from petapp.models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(ItemType)
admin.site.register(ItemBrand)
admin.site.register(ItemNeed)
admin.site.register(ItemListing)
admin.site.register(Message)
