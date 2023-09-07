from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    picture = models.FileField()
    category = models.CharField(max_length=20, choices=(
        ("TECH", "Technology"),
        ("FOOD", "Food"),
        ("TRAV", "Traveling"),
        ("PET", "Pet Food"),
        ("TEST", "Testing"),
    ), default=None)
    datetime = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=120)
    content = RichTextField()
