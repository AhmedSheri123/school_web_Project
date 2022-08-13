from django.contrib import admin
from .models import UserProfile, Levels, BlodsType, PassData, DefindedNumbers
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Levels)
admin.site.register(BlodsType)
admin.site.register(PassData)
admin.site.register(DefindedNumbers)