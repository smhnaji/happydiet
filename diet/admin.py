from django.contrib import admin
from .models import *

# Register your models here.
class DietPlanAdmin(admin.ModelAdmin):
    pass

class DietPlanSubscriptionAdmin(admin.ModelAdmin):
    pass

class DietOrderAdmin(admin.ModelAdmin):
    pass

class DietAdmin(admin.ModelAdmin):
    pass

admin.site.register(DietPlan)
admin.site.register(DietPlanSubscription)
admin.site.register(DietOrder)
admin.site.register(Diet)