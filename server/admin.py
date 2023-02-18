from django.contrib import admin
from .models import Specification, Experience, Education


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'about', 'age', 'email', 'phone')
    # list_filter = ('full_name', 'title', 'about', 'age', 'email', 'phone')
    # search_fields = ('full_name', 'title', 'about', 'age', 'email', 'phone')


@admin.register(Experience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'description', 'start_date', 'end_date')
    # list_filter = ('title', 'company', 'description', 'start_date', 'end_date')
    # search_fields = ('title', 'company', 'description', 'start_date', 'end_date')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'fromm', 'start_date', 'end_date')
    # list_filter = ('title', 'fromm', 'start_date', 'end_date')
    # search_fields = ('title', 'fromm', 'start_date', 'end_date')

