from django.shortcuts import render

# Create your views here.
def sample1(request):
    d={'name':'abhijith','age':23}
    return render(request,'sample1.html',context=d)