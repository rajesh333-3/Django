from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Credentials
import datetime
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
    all_apps_list=Credentials.objects.all()
    #print(all_app_list)
    return render(request,'myvault/home.html', {'all_apps_list':all_apps_list,})

def reveal(request,app_id):
    try:
        app = get_object_or_404(Credentials,app_name=app_id)
        #print(app)
    except Credentials.DoesNotExist:
        return HttpResponseRedirect(reverse('myvault:add_credential'))
    return render(request, 'myvault/reveal.html', {'app': app})

def new_cred(request):
    return render(request,'myvault/new_cred.html')

def delete_cred(request, app_id):
    try:
        a = get_object_or_404(Credentials,app_name=app_id)
        #print(app)
        a.delete()
    except Credentials.DoesNotExist:
        return HttpResponseRedirect(reverse('myvault:add_credential'))
    
    return render(request,'myvault/sucess.html')

def add_credential(request):
    app_name_input = request.POST['applic']
    username_input= request.POST['user']
    password_input= request.POST['pass']
    description_input= request.POST['desc']
    last_updated_input=datetime.datetime.now()
    new_cred=Credentials(app_name=app_name_input,username=username_input,password=password_input,description=description_input,last_updated=last_updated_input)
    new_cred.save()
    return render(request,'myvault/sucess.html')