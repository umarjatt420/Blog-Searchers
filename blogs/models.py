from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    picture = models.FileField()
    category = models.CharField(max_length=20, choices=(
        ("AI", "Artificial Intelligence"),
        ("IT", "Information Technology"),
        ("CN", "Computer Network"),
        ("PROGRAMMING", "Programming"),
        ("ROBOTICS", "Robotics"),
        ("QC", "Quantum Computing"),
        ("DS", "Data Science"),
        ("AUTOMATION", "Automation"),
        ("VR", "Virtual Reality"),
    ), default=None)
    datetime = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=120)
    content = RichTextField()
