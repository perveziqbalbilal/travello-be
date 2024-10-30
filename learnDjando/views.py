from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def add(request):
    valu1 = request.POST['num1']
    valu2 = request.POST['num2']
    res = valu1 + valu2
    return render(request, 'result.html',{'result': res})
    
# def home(request):
#     return HttpResponse('home new')