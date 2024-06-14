from django.shortcuts import get_object_or_404,redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from jitter.models import Bunk, User, Bunkform
from django.template import loader
from django.urls import reverse
from .forms import BunkFormm

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
  #  return render(request, "index.html")
    return HttpResponse(template.render(context,request))
def bunkform(request):
    # if request.POST:

    #     form = Bunkform(request.POST, request.POST)
    #     if form.username and form.other_user:
    #         form.save()
    #     return redirect(index)
    # return render(request, "jitter/bunkform.html", {"form": Bunkform})
    print(1)
    if request.method =='POST':
       
        form = BunkFormm(request.POST, request.POST)
        print(2)
        print(form.is_valid())
        if request.POST['your_name'] and request.POST['other_name']:
            
            form.save()
        else:
            
            print("hi")
            return render(request, 'jitter/index.html')
        
    else: 
        form = BunkFormm()
    return render(request, 'jitter/bunkform.html', {"form": form})
       
    




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
