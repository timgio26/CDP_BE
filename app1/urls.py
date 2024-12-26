from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('customer/', views.CustomerList.as_view()),
    path('customer/<int:pk>/', views.CustomerDetail.as_view()),
    path('address/', views.AddressView.as_view()),
    path('address/<int:pk>/', views.AddressEachView.as_view()),
    path('service/', views.ServiceView.as_view()),
    path('service/<int:pk>/', views.ServiceEachView.as_view()), 
]

urlpatterns = format_suffix_patterns(urlpatterns)