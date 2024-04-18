from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from seller.models import Products, Category

def index(request):
    object_list = Products.objects.all()
    context = {
        'object_list':object_list
    }
    return render(request, 'home.html', context)

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register.html')

class UserCreateDoneTV(TemplateView):
    template_name='registration/register_done.html'