from django.db import models

# Create your models here.

class PersonalData(models.Model):
  

    
    surname = models.CharField(max_length=264)
    othername = models.CharField(max_length=264)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    state = models.CharField(max_length=100, blank=True)
    address = models.TextField(max_length=500, blank=True)   
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = "info"
	verbose_name_plural = "infos"
