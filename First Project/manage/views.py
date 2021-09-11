from django.http.response import HttpResponse
from manage import models
from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from gym.models import * 
from manage.models import trainers
# Create your views here.

def login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
	
		user = auth.authenticate(request,username=username,password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('adminpage')
		else:
			messages.error(request,'username or password not correct')
			return redirect('login')	
	else:
		return render(request,'manage/login.html')		
	return render(request,'manage/login.html')		

def enquiry(request):
	enq = enquiries.objects.all()
	d = {'enq':enq}
	return render(request,'manage/ViewEnquiry.html',d)

def gymTrainers(request):
	trainer = trainers.objects.all()
	d = {'trainer':trainer}
	return render(request,'manage/trainers.html',d)

def equipment(request):
	eqp = equipments.objects.all()
	d = {'eqp':eqp}
	return render(request,'manage/equipments.html',d)

def addEquipment(request):
	if request.method == "POST":
		name = request.POST['name']
		quantity = request.POST['quantity'] 
		modelno = request.POST['model']
		eqtype = request.POST['type']
		price = request.POST['price']
		warranty = request.POST['war_per']
		warr =  warranty + ' years'
		dop = request.POST['dop']

		equipments.objects.create(eq_name = name,units = quantity,model_no = modelno,eq_type = eqtype,price = price,warranty = warr,date_of_pur = dop)
		return redirect('equipments')
	return render(request,'manage/addEquipment.html')


def fees(request):
	f = fee.objects.all()
	d = {'f':f}
	return render(request,'manage/fees.html',d)  
	

def member(request):
	members = gym.objects.all()
	d = {'members':members}
	return render(request,'manage/members.html',d)

def addMemmber(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		age = request.POST['age']
		phone = request.POST['cell']
		dob = request.POST['dob']
		gender = request.POST['gender']
		plan = request.POST['plan']

		gym.objects.create(full_name=name,gender=gender,age=age,cell_no=phone,born_date=dob,email=email,plan=plan)
		return redirect('members')
	return render(request,'manage/addMember.html')

def logout(request):
	auth.logout(request)
	return redirect('gym:home')

def updateFee(request,pid):
	f = fee.objects.get(id=pid)
	if f.paid_status == True:
		f.paid_status = False
	else:
		f.paid_status = True	
	f.save()

	return redirect('fee')

def deleteEnq(request,pid):
	e = enquiries.objects.get(id=pid)
	e.delete()
	return redirect('enquiry')


def sched(request):
	days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
	sch = schedule.objects.all()
	d = {'sch':sch,'days':days}
	return render(request,'manage/schedule.html',d)	

def addSched(request):
	if request.method == 'POST':
		name = request.POST['name']
		mon = request.POST['mon']
		tue = request.POST['tue']
		wed = request.POST['wed']
		thu = request.POST['thu']
		fri = request.POST['fri']
		sat = request.POST['sat']
		train = request.POST['train']

		n = gym.objects.get(full_name=name)
		t = trainers.objects.get(trainer_name=train)

		schedule.objects.create(client=n,mon=mon,tue=tue,wed=wed,thu=thu,fri=fri,sat=sat,trainer=t)
		return redirect('schedule')
	trainer = trainers.objects.all()
	d = {'trainer':trainer}
	return render (request,'manage/addSchedule.html',d)


def addTrainer(request):
	if request.method == 'POST':
		name = request.POST['name']
		age = request.POST['age']
		cell = request.POST['cell']
		salary = request.POST['salary']
		gender = request.POST['gender']	
		spl = request.POST['spl']

		trainers.objects.create(trainer_name=name,trainer_age=age,trainer_gender=gender,trainer_cell=cell,aos=spl,salary=salary)
		return redirect('trainers')	
	return render(request,'manage/addTrainer.html')

@login_required
def adminPage(request):
	return render(request,'manage/adminPage.html')