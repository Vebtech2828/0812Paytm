from django.shortcuts import render
from Online_Payments.models import employee

# Create your views here.


def Home1(request):
    return render(request, 'result.html')


def Home2(request):
    return render(request, 'payment.html')


def empdata(request):
    emp_list = employee.objects.all()
    my_dict = {'emp_list': emp_list}
    return render(request, 'Online_Payments/employee.html', context=my_dict)