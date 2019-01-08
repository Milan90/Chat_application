from django.http import HttpResponse
from django.shortcuts import render
from ChatApp.forms import *
# Create your views here.
from django.views import View


class UserRegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'ChatApp/registration.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data.get('username'),
                                            first_name=form.cleaned_data.get('first_name'),
                                            last_name=form.cleaned_data.get('last_name'),
                                            email=form.cleaned_data.get('email'),
                                            password=form.cleaned_data.get('password'))
            return HttpResponse("zarejstrowano pomyślnie")
        else:
            return render(request, 'ChatApp/registration.html', {'form': form})
