from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from tasklister.forms import *
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def dep1(request):
    # show all users and tasks assigned ( tasks pulled from admin)
    return render(request, 'dep1.html', {"objects": Task.objects.filter(department=DEPARTMENT1)})

def dep2(request):
    # show all users and tasks assigned ( tasks pulled from admin)
    return render(request, 'dep2.html', {"objects": Task.objects.filter(department=DEPARTMENT2)})

def updateStatus(request):
    status = request.POST.get('staus', '')
    return render(request, 'index.html')


def adduser(request):
    usr = UserForm()
    if request.method == 'POST':
        usr = UserForm(request.POST)
        if usr.is_valid():
            usr.save()
            return HttpResponseRedirect("/index")
    return render(request, "adduser.html", {'form': usr})


def fubar(request):
    op_val = request.GET.get('val')
    print(op_val)
    aj_id = request.GET.get('val2')
    for task in Task.objects.all():
        if task.id == int(aj_id) :
            task.status = op_val
            task.save()
    return JsonResponse({'success': op_val})
