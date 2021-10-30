"""SampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from manage import views as manage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gym.urls')),

    path('login',manage_views.login, name = 'login'),
    path('logout',manage_views.logout,name = 'logout'),
    path('AdminPage/dashboard',manage_views.adminPage,name='adminpage'),

    path('AdminPage/enquiries',manage_views.enquiry,name='enquiry'),
    path('AdminPage/del_status(?p<int:pid>)',manage_views.deleteEnq,name='delEnq'),

    path('AdminPage/members',manage_views.member,name='members'),
    path('AdminPage/members/add',manage_views.addMemmber,name='AddMember'),

    path('AdminPage/trainers',manage_views.gymTrainers,name='trainers'),
    path('AdminPage/trainers/add',manage_views.addTrainer,name='addTrainer'),

    path('AdminPage/equipments',manage_views.equipment,name='equipments'),
    path('AdminPage/equipments/add',manage_views.addEquipment,name='AddEquipment'),

    path('AdminPage/fees',manage_views.fees,name='fee'),
    path('AdminPage/Update_status(?p<int:pid>)',manage_views.updateFee,name='updatefee'),

    path('AdminPage/schedule',manage_views.sched,name='schedule'),
    path('AdminPage/schedule/add_schedule',manage_views.addSched,name='addsch')



    
]
