from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import *
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
	members = fee.objects.all()
	if request.method == 'POST':
		name = request.POST['paid_member']
		mem_id = request.POST['id']

		f = fee.objects.get(id=mem_id)
		f.paid_status = True
		f.save()
		return redirect('gym:home')
	ExpiryDate = {
	'months' : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
	'years' : [2021,2022,2023,2024,2025,2026,2027,2028,2029,2030] }
	return render(request,'gym/payment.html',{'dates':ExpiryDate})
	
	

def membership(request):
	
	if request.method == 'POST':
		name = request.POST['member']
		age = request.POST['age']
		email = request.POST['emailid']
		gender = request.POST['gender']
		cell = request.POST['cell']
		pack = request.POST['plan']
		dob = request.POST['DOB']

		gym.objects.create(full_name=name,gender=gender,age=age,cell_no=cell,born_date=dob,email=email,plan=pack)
		fee.objects.update()
		return redirect('gym:home')
	ExpiryDate = {
		'months' : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
	 	'years' : [2021,2022,2023,2024,2025,2026,2027,2028,2029,2030] }
	return render(request,'gym/membership.html',{'dates':ExpiryDate})

#PDF GENERATOR

from django.template.loader import get_template
from xhtml2pdf import pisa

def render_pdf_view(request):
    template_path = 'gym/pdf.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response 