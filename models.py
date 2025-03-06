from django.db import models

# Create your models here.
class Blogname(models.Model):
    blogname = models.CharField(max_length=50)
    description = models.EmailField(max_length=50)
    image = models.ImageField(upload_to='images')
    
    def _str_(self): 
        return self.blogname