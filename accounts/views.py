from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import NameForm, LoginForm
from django.http import HttpResponseRedirect

# Create your views here.
class SignUp(generic.CreateView):
    form_class = NameForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = authenticate(username=username)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/hunts')
            else:
                return HttpResponseRedirect('/hunts')
        else:
            return HttpResponseRedirect('/hunts')
    form = LoginForm()
    return render(request = request,
                    template_name = "registration/login.html",
                    context={"form":form})