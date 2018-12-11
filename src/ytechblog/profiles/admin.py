from django.contrib import admin

from .models import Airport, Flight, Passenger

# Register your models here.
from .models import profile

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)

class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = profile

admin.site.register(profile, profileAdmin)