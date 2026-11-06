from django.shortcuts import render, redirect
from .models import Department, Service, FAQ, Appointment, Doctor

def home_view(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        date = request.POST.get('date')
        message = request.POST.get('message')

        Appointment.objects.create(
            patient_name=patient_name,
            phone=phone,
            department=department,
            date=date,
            message=message
        )
        return redirect('home')

    departments = Department.objects.all()
    services = Service.objects.all()
    faqs = FAQ.objects.all()
    doctors = Doctor.objects.all()
    
    context = {
        'departments': departments,
        'services': services,
        'faqs': faqs,
        'doctors': doctors,
    }
    return render(request, 'main/index.html', context)

def about_view(request):
    return render(request, 'main/about.html')

def empanelments_view(request):
    return render(request, 'main/empanelments.html')

def doctors_page_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'main/doctors.html', {'doctors': doctors})

def service_detail_view(request, slug):
    service = Service.objects.filter(slug=slug).first()
    
    if not service:
        service_name = slug.replace('-', ' ').title()
        context = {
            'title': service_name,
            'summary': f'Welcome to the detailed page for {service_name} at Nova Hospital. We offer complete care and treatment.',
        }
    else:
        context = {
            'title': service.title,
            'summary': service.summary,
        }
        
    return render(request, 'main/service_detail.html', context)

def news_view(request):
    return render(request, 'main/news.html')

def blogs_view(request):
    return render(request, 'main/blogs.html')

def contact_view(request):
    return render(request, 'main/contact.html')

def appointment_page_view(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        phone = request.POST.get('phone')
        dept_name = request.POST.get('department') 
        date = request.POST.get('date')
        message = request.POST.get('message')
        
        
        department_obj = Department.objects.filter(name=dept_name).first()
        
        
        Appointment.objects.create(
            patient_name=patient_name,
            phone=phone,
            department=department_obj,  
            date=date,
            message=message
        )
        return redirect('/?status=success')
        
    return render(request, 'main/appointment.html')