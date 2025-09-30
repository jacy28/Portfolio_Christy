from django.db import models

# Create your models here.
class Skill(models.Model):
    name=models.CharField(max_length=255)
    icon=models.ImageField(upload_to='skills/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='projects/', blank=True, null=True)
    desc=models.TextField()
    link=models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

