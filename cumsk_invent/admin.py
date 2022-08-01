from django.contrib import admin
from .models import Nodetable, CiscoDs, Esmacards, Pingariumresults, Hardwareinfo

# Register your models here.

admin.site.register(Nodetable)
admin.site.register(CiscoDs)
admin.site.register(Esmacards)
admin.site.register(Hardwareinfo)
admin.site.register(Pingariumresults)
