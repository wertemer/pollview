from django.contrib import admin
from oprosnik.models import Questions, Answers, Users, UserAnswers,Opros

# Register your models here.

admin.site.register(Opros)
admin.site.register(Answers)
admin.site.register(Questions)
admin.site.register(Users)
admin.site.register(UserAnswers)
