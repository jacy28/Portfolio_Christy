from django.shortcuts import render
from .models import Skill, Project
from django.core.mail import send_mail
from django.http import JsonResponse

def home(request):
    skills=Skill.objects.all()
    projects=Project.objects.all()
    success = None 

    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message_text=request.POST.get('message')

        try:
            # Email to you
            send_mail(
                subject=f"New message from {name}",
                message=f"From: {name} <{email}>\n\n{message_text}",
                from_email="christy.methila@gmail.com",
                recipient_list=["christy.methila@gmail.com"],
            )

            # Confirmation to sender
            send_mail(
                subject="Thanks for contacting me!",
                message=f"Hi {name},\n\nThanks for reaching out! I have received your message and will get back to you soon.",
                from_email="christy.methila@gmail.com",
                recipient_list=[email],
            )

            return JsonResponse({"success": "Your message has been sent successfully!"})
        except:
            return JsonResponse({"success": None})

    return render(request, 'portfolio/home.html', {'skills':skills, 'projects':projects, 'success':success})

