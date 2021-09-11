from django.urls import path
from . import views
app_name = 'gym'
urlpatterns = [
    
    path('',views.home, name = 'home'),
    path('plans/',views.plans, name = 'plans'),
    path('payment/',views.payment,name ='payment'),
    path('membership/',views.membership,name='membership'),
    path('transaction_status/',views.paySucc,name='psuccess'),
    path('membership_success/',views.memsuc,name='msuccess'),
    path('invoice/',views.render_pdf_view,name="pdf")
]
