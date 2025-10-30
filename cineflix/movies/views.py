from django.shortcuts import render

from django.views import View

# Create your views here.

class HomeView(View):

    def get(self,request,*args,**kwargs):

        data = {'page' : 'home'}

        return render(request,'home.html',context=data)
