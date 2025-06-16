from django.contrib import admin
from .models import Course, CourseMember

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'price')
    search_fields = ('name', 'teacher')
    list_filter = ('teacher',)

@admin.register(CourseMember)
class CourseMemberAdmin(admin.ModelAdmin):
    list_display = ('course', 'user_id', 'roles')
    list_filter = ('roles',)
    search_fields = ('course__name', 'user_id')
