from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Product(models.Model):
    LANGUAGE_CHOICES = (
        ('en', 'English'),
        ('fr', 'French'),
        ('ar', 'Arabic'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = CloudinaryField('image', blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, default='en')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', null=True, blank=True)


    def __str__(self):
        return self.name
class Category(models.Model):
    LANGUAGE_CHOICES = (
        ('en', 'English'),
        ('fr', 'French'),
        ('ar', 'Arabic'),
    )
    name = models.CharField(max_length=100)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, default='en')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'