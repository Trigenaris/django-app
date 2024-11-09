from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=200, verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    article_img = models.FileField(blank=True, null=True, verbose_name="Makale Fotoğrafı")
    is_approved = models.BooleanField(default=False, verbose_name="Onaylı mı?")

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Yorum")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    
    def __str__(self):
        return self.author.username
    

class FooterSettings(models.Model):
    description = models.TextField(verbose_name="Şirket Açıklaması", blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="Adres", blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name="Telefon", blank=True, null=True)
    email = models.EmailField(verbose_name="E-posta", blank=True, null=True)
    facebook = models.URLField(verbose_name="Facebook URL", blank=True, null=True)
    instagram = models.URLField(verbose_name="Instagram URL", blank=True, null=True)
    twitter = models.URLField(verbose_name="Twitter URL", blank=True, null=True)
    linkedin = models.URLField(verbose_name="Linkedin URL", blank=True, null=True)

    def __str__(self):
        return "Footer Ayarları"

class Service(models.Model):
    title = models.CharField(max_length=150, verbose_name=" Başlık")
    description = models.TextField(verbose_name="Açıklama")
    created_date = models.DateTimeField(auto_now_add=True)
    service_image = models.ImageField(upload_to="service_manager", blank=True, null=True, verbose_name="Resım")

    def __str__(self):
        return self.title