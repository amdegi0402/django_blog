from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import BlogModel
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.contrib.auth.models import User


def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            User.objects.create_user(username_data, '', password_data)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'すでに登録されています。'})
        #user = User.objects.create_user(username_data, '', password_data)
        #print('POST method')
    else:
        return render(request, 'signup.html', {})
    return render(request, 'signup.html', {})

class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel
class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel
class BlogCreate(CreateView):
    template_name = 'create.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')
class BlogDelete(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')
class BlogUpdate(UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')