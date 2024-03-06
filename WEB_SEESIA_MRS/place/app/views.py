
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.views import View
from .forms import AppointmentForm, PostForm
from .models import Appointment, Post


def home(request):
    posts = Post.objects.all()
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'index.html', {'posts': posts, 'form': form})


class AppointmentView(View):
    template_name = 'appointment.html'

    def get(self, request):
        form = AppointmentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info')  # Используем именованный путь 'info'
        return render(request, self.template_name, {'form': form})


def info_view(request):
    appointments = Appointment.objects.all()
    return render(request, 'info.html', {'appointments': appointments})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'post.html', {'form': form})