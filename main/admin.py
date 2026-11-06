from django.contrib import admin
from .models import Blog, Department, Doctor, Service, Appointment, FAQ , News 

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'qualification', 'specialization', 'department')
    search_fields = ('name', 'specialization')
    list_filter = ('department',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'phone', 'department', 'date', 'created_at')
    list_filter = ('department', 'date')
    search_fields = ('patient_name', 'phone')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    prepopulated_fields = {'slug': ('title',)}