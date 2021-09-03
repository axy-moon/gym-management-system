from django.db import models

# Create your models here.

class trainers(models.Model):
	trainer_name = models.CharField(max_length=30,verbose_name='Name')
	trainer_age = models.IntegerField(verbose_name='Age')	
	trainer_gender = models.CharField(max_length=10,verbose_name='Gender')
	trainer_cell = models.IntegerField(verbose_name='Mobile No',null=True)
	aos = models.CharField(max_length=100,verbose_name='Area of Specialization')
	clients = models.IntegerField(verbose_name='Number of Clients')
	salary = models.IntegerField(verbose_name='Salary')
	
	class Meta:
		verbose_name_plural = 'Trainers'

	def __str__(self):
		return self.trainer_name