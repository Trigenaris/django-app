from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class About(models.Model):
    title = models.CharField(max_length=255, verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")

    def __str__(self):
        return self.title