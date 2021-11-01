from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import *
import random
 # Create your views here.

def home(request):
	if request.method == 'POST':
		emailid = request.POST['enq_email']
		enquiry = request.POST['enquiry']

		enquiries.objects.create(email=emailid,Enquiry=enquiry)
		return redirect('gym:home')
	else:	
		return render(request,'gym/index.html')

def plans(request):	
		return render(request,'gym/plans.html')	



def payment(request):
	f = fee.objects.all()
	if request.method == 'POST':
		name = request.POST['paid_member']
		mem_id = request.POST['id']

		if mem_id not in f:
			return HttpResponse("Member not Found")

		fee.objects.filter(pk=mem_id).update(paid_status=True)
		return redirect('gym:psuccess')
	ExpiryDate = {
	'months' : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
	'years' : [2021,2022,2023,2024,2025,2026,2027,2028,2029,2030] }
	return render(request,'gym/payment.html',{'dates':ExpiryDate})
	
def paySucc(request):
	trans_id = ""

	for i in range(9):
		trans_id += str(random.randint(1,10))

	d = {'t_id' : trans_id}
	return render(request,'gym/paysucess.html',d)	
	
def membership(request):
	
	if request.method == 'POST':
		name = request.POST['member']
		age = request.POST['age']
		email = request.POST['emailid']
		gender = request.POST['gender']
		cell = request.POST['cell']
		pack = request.POST['plan']
		dob = request.POST['DOB']
		
		numbers = "1234567890"
		alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		a = numbers + alpha_upper
		length = 12
		trans_id = "".join(random.sample(a,length))
		gym.objects.create(full_name=name,gender=gender,age=age,cell_no=cell,born_date=dob,email=email,plan=pack,trans=trans_id)
		return redirect('gym:msuccess')
	ExpiryDate = {
		'months' : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
	 	'years' : [2021,2022,2023,2024,2025,2026,2027,2028,2029,2030] }
	return render(request,'gym/membership.html',{'dates':ExpiryDate})

def memsuc(request):
	g = gym.objects.filter().order_by('-date_joined')[:1]
	con = {'g':g}
	return render(request,"gym/memsucess.html",con)

# #PDF GENERATOR

# from django.template.loader import get_template
# from xhtml2pdf import pisa

# def render_pdf_view(request):
#     template_path = 'gym/pdf.html'
#     context = {'myvar': 'this is your template context'}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response)
#     # if error then show some funy view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response 