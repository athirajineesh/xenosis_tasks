from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team

# Create your views here.
def registration(request):
   # name="India"
   obj=Place.objects.all()
   member=Team.objects.all()
   return render(request,"index.html",{'value':obj,'person':member}) #{'change':name})
#def add(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # res=x+y
    #return render(request,"result.html",{'output':res})
