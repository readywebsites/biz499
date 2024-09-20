from django.contrib import admin

# Register your models here.
from .models import Team, Category, Blog_Post,Pricecard,Portfolio,Project_Strategy,Project_Category,Project_Design

admin.site.register(Team)
admin.site.register(Category)

class Blog_PostAdmin(admin.ModelAdmin):
    readonly_fields = ('Timestamp',)
admin.site.register(Blog_Post,Blog_PostAdmin)

admin.site.register(Pricecard)
admin.site.register(Portfolio)
admin.site.register(Project_Strategy)
admin.site.register(Project_Category)
admin.site.register(Project_Design)