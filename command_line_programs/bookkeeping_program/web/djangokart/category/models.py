from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    category_image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    
    class Meta :
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.category_name