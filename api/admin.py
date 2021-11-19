from django.contrib import admin
from .models import Survey, SurveyQuestions, UserResponse, Choice

# Register your models here.

admin.site.register(Survey)
admin.site.register(SurveyQuestions)
admin.site.register(UserResponse)
admin.site.register(Choice)