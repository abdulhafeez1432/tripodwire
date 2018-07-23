from django.db import models

# Create your models here.

class PersonalData(models.Model):
	fullname = models.CharField(max_length=264)
	email = models.EmailField(max_length=254, unique=True)

	def __str__(self):
		return self.fullname

	class Meta:
		verbose_name = "info"
		verbose_name_plural = "infos"
