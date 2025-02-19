from django.shortcuts import render
from .models import Resume

def display_cv(request):
    resume = Resume.objects.first()  # Fetch the first resume (or filter by user if needed)
    
    # Split experience into a list of items (assuming '\n\n' separates entries)
    experience_list = resume.experience.split('\n\n') if resume and resume.experience else []
    
    return render(request, 'cv/display_cv.html', {
        'resume': resume,
        'experience_list': experience_list  # Pass the processed list to the template
    })
