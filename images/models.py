from django.db import models
from services import predict 
from django.shortcuts import redirect, reverse

class Image(models.Model):
	image = models.ImageField(upload_to = 'images/%Y/%m/%d')
	
	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		super().save(force_insert=force_insert, force_update=force_update, using=using,update_fields=update_fields)
		self.res = predict.predict_result(self.image.url)
