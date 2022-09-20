from multiprocessing import context
from re import template
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import *
from .models import ListItem, ListName
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        template = 'home.html'
        form = ListForm()
        lists = ListName.objects.filter(user=request.user)
        context = {'form': form, 'lists': lists}
        return render(request, template, context)
    else:
        template = 'home.html'
        return render(request, template)

def add_list(request):
    ln = request.POST['list_name']
    user = request.user
    list_name = ListName(list_name=ln, user=user)
    list_name.save()
    return HttpResponseRedirect('/')

def del_list(request, n):
    x = ListName.objects.get(id=n)
    x.delete()
    return HttpResponseRedirect('/')

def edit_list(request, n):
    template = 'edit_list.html'
    e = ListName.objects.get(id=n)
    form = EditListForm(initial={'list_name': e})
    context = {'form': form, 'list_name': e}
    return render(request, template, context)

def update_list(request, n):
    up = request.POST['list_name']
    ln = ListName.objects.get(id=n)
    ln.list_name = up
    ln.save()
    return HttpResponseRedirect('/')

def list_page(request, n):
    template = 'list_page.html'
    lname = ListName.objects.get(id=n)
    form = AddItemForm()
    li = ListItem.objects.filter(list=lname)
    context = {'form': form, 'list_items': li, 'list_name': lname}
    return render(request, template, context)

def add_item(request, n):
    lname = ListName.objects.get(id=n)
    item = request.POST['list_item']
    user = request.user
    litem = ListItem(list=lname, list_item=item, user=user)
    litem.save()
    return HttpResponseRedirect('/list_page/' + str(n) + '/')

def del_item(request, l, i):
    x = ListItem.objects.get(id=i)
    x.delete()
    return HttpResponseRedirect('/list_page/' + str(l) + '/')

def edit_item(request, l, i):
    template = 'edit_item.html'
    e = ListItem.objects.get(id=i)
    ln = ListName.objects.get(id=l)
    form = EditItemForm(initial={'list_item': e.list_item})
    context = {'form': form, 'list_item': e, 'list': ln}
    return render(request, template, context)

def update_item(request, l, i):
    u = request.POST['list_item']
    list_item = ListItem.objects.get(id=i)
    ln = ListName.objects.get(id=l)
    list_item.list_item = u
    list_item.save()
    return HttpResponseRedirect('/list_page/' + str(ln.id) + '/')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template = 'registration/signup.html'
    success_url = reverse_lazy('index')

def demo_login(request):
    user = authenticate(username='Demo', password='demopassword')
    login(request, user)
    demo_items = ListName.objects.filter(user=user)
    demo_items.delete()
    return redirect('/')
