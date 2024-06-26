from django.shortcuts import get_object_or_404,redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from jitter.models import Bunk, User, Bunkform
from django.template import loader
from django.urls import reverse
from .forms import BunkFormm
from datetime import datetime

def index(request):

    return render(request, 'jitter/index.html')
def mainbunk(request):
    latest_bunks_list = Bunk.objects.all()
#    output = ', '.join([q.username for q in latest_bunks_list])
    template = loader.get_template('jitter/mainbunk.html')
    context = {'latest_bunks_list' : latest_bunks_list,
    } 
  #  return render(request, "index.html")
    return HttpResponse(template.render(context,request))


def mainuser(request):
    latest_users_list = User.objects.all()
#    output = ', '.join([q.username for q in latest_bunks_list])
    template = loader.get_template('jitter/mainuser.html')
    context = {'latest_users_list' : latest_users_list,
    } 
    return HttpResponse(template.render(context,request))
def bunkform(request):
   
    if request.method =='POST':
       
        form = BunkFormm(request.POST)
      
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            other_name = form.cleaned_data['other_name']
            if not User.objects.filter(username=your_name) or not User.objects.filter(username=other_name):
                return render(request, 'jitter/formfailed.html')

            # if User.objects.get(username=your_name)
            bunkform = Bunkform(your_name=your_name, other_name=other_name)
            bunkform.save()
            user1 = User.objects.get(username=your_name)
            user2 = User.objects.get(username=other_name)
            addbunk = Bunk(from_user=user1, to_user=user2, time=datetime.now())
            addbunk.save()
            return render(request, 'jitter/formsuccess.html')
        else:
            
          
            return render(request, 'jitter/formfailed.html')
        
    else: 
        form = BunkFormm()
    return render(request, 'jitter/bunkform.html', {"form": form})
       
    
def formfailed(request):

    return render(request, 'jitter/formfailed.html')

def formsuccess(request):

    return render(request, 'jitter/formsuccess.html')


def view_bunks(request,pk):   
    user = User.objects.get(id=pk)
    usern = user.username
    givebunks = Bunk.objects.filter(from_user__username=usern)
    print(user)
    gotbunks = Bunk.objects.filter(to_user__username=usern)
   
    context = {
        "user": user,
      
        "givebunks":givebunks,
        "gotbunks":gotbunks,
    }
    return render(request, "jitter/userbunk.html", context)
