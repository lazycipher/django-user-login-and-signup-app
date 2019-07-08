from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.models import User
from accounts.forms import UserForm
from django.shortcuts import render

def SignUp(request):
    registered = False
    if(request.method == 'POST'):
        user_form = UserForm(data=request.POST)
        if user_form.is_valid() and user_form.cleaned_data['password'] == user_form.cleaned_data['confirm_password']:
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        elif user_form.data['password'] != user_form.data['confirm_password']:
            user_form.add_error('confirm_password', 'Passwords does not match')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'registration/signup.html',
                          {'user_form':user_form,
                           'registered':registered})

class Login(generic.CreateView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('')
    template_name = 'registration/login.html'

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
