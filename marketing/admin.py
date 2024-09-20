from django.contrib import admin

# Register your models here.
from .models import OrderUpdate,Payment,Subscription,New_Project,New_Project,Open_posts,Job_applications, Subscription,Home_services,Home_logos,Lead

class SubscriptionAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)
admin.site.register(Subscription,SubscriptionAdmin)



class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('pk',)
admin.site.register(Payment, PaymentAdmin)

admin.site.register(New_Project)
admin.site.register(Open_posts)
admin.site.register(Job_applications)
admin.site.register(Home_services)
admin.site.register(Home_logos)
admin.site.register(OrderUpdate)
admin.site.register(Lead)

