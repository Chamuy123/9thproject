from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':2056,'b':23400,'c':10000000}
    return render(request,'conditions.html',d)
