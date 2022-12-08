from django.urls import path
from Online_Payments import views
from Online_Payments.views import employee

urlpatterns = [
    path('Home1/', views.Home1),
    path('Home2/', views.Home2),
    path('Emp/', employee)
]