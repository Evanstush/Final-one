
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.home, name='index'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('myservice/', views.myservice, name='services'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('contactpreview/', views.contactpreview, name='contactpreview'),
    path('deletecontact/<int:id>', views.deletecontact),
    path('edit/<int:id>', views.edit ,name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),

#Mpesa urls
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),

]