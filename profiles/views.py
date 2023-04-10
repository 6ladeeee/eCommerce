from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Order


def login(request):
    profile = request.user.username
    context = {
        'profile': profile,
        'orders': Order.objects.filter(user=request.user),
    }
    return render(request, 'account/profile.html', context)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/registration.html'


def logout_view(request):
    logout(request)
    return redirect('index')
