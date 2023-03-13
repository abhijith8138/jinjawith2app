from django.shortcuts import render

# Create your views here.
def sample2(request):
    d={'name':'sreekutty','age':22}
    return render(request,'sample2.html',context=d)