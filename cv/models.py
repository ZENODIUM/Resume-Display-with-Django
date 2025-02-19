from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    linkedin = models.URLField()
    github = models.URLField()
    kaggle = models.URLField()
    education = models.TextField()
    experience = models.TextField()
    projects = models.TextField()
    skills = models.TextField()
    competitions = models.TextField()
    resume_file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name
