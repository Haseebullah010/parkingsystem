from django.contrib import admin

from parking.models import parking1,parking2,parking3,parking4,overalldata

# Register your models here.
admin.site.register(overalldata)
admin.site.register(parking1)
admin.site.register(parking2)
admin.site.register(parking3)
admin.site.register(parking4)