from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_DEFAULT
from django.db.models.fields import AutoField, CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from manage.models import trainers
# Create your models here.

class gym(models.Model):
	full_name = models.CharField(max_length=100)
	gender = models.CharField(max_length=7)
	age = models.IntegerField(default=18)
	cell_no = models.IntegerField()
	born_date = models.DateField(null=True,default=None,blank=True)
	email = models.EmailField()
	plan = models.CharField(max_length=10,default='Silver',null=False)
	date_joined = models.DateTimeField(default=timezone.now)
	

	def __str__(self):
		return self.full_name


class enquiries(models.Model):
	email = models.EmailField(max_length=100)
	Enquiry = models.TextField()	

	class Meta:
		verbose_name_plural = 'Enquiries'
	
	def __str__(self):
		return self.email

	

class equipments(models.Model):
	eq_name = models.CharField(max_length=30,verbose_name='Name',null=True)
	units = models.IntegerField(default=1,verbose_name='Quantity')
	model_no = models.CharField(max_length=30,verbose_name='Model No',null=True)
	eq_type = models.CharField(max_length=30,verbose_name='Type',default='Cardio')
	price = models.IntegerField(verbose_name='Price',null=True)
	warranty = models.CharField(max_length=100,verbose_name='Warranty Period',default='1 year')
	date_of_pur = models.DateField(default='2021-08-08',verbose_name='Date of Purchase')

	class Meta:
		verbose_name_plural = 'Equipments'

	def __str__(self):
		return self.eq_name
	

class schedule(models.Model):
	client = models.ForeignKey(gym,on_delete=CASCADE)
	mon = models.CharField(max_length=100,default=1,verbose_name='Monday')
	tue = models.CharField(max_length=100,default=1,verbose_name='Tuesday')
	wed = models.CharField(max_length=100,default=1,verbose_name='Wednesday')
	thu = models.CharField(max_length=100,default=1,verbose_name='Thursday')
	fri = models.CharField(max_length=100,default=1,verbose_name='Friday')
	sat = models.CharField(max_length=100,default=1,verbose_name='Saturday')
	trainer = models.ForeignKey(trainers,on_delete=CASCADE)

	def __str__(self):
		return self.client.full_name

class packages(models.Model):

	plan_name = models.CharField(max_length=10,default="Silver",verbose_name='Plan Name')
	plan_type = models.CharField(max_length=100,default='Monthly',verbose_name='Type')
	plan_amt = models.IntegerField(default=1000,verbose_name='Amount')

class fee(models.Model):
	member = models.ForeignKey(gym,on_delete=CASCADE,default=1,verbose_name='Member Name')
	paid_status = models.BooleanField(default=False,verbose_name='Status')

	def __str__(self):
		return self.member.full_name