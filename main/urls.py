from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about-nova/', views.about_view, name='about_nova'),
    path('empanelments/', views.empanelments_view, name='empanelments'),
    path('doctors/', views.doctors_page_view, name='doctors_page'),
    path('service/<slug:slug>/', views.service_detail_view, name='service_detail'),
    path('news-media/', views.news_view, name='news_media'),
    path('blogs/', views.blogs_view, name='blogs'),
    path('contact-us/', views.contact_view, name='contact_us'),
    path('book-appointment/', views.appointment_page_view, name='book_appointment'),
]