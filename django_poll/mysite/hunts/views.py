from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.views import generic

from .models import HuntClue, ClueAnswer, Hunt, Stop, Answer, Response, Usrs, Corrects
##from ../accounts/views import SignUp
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

from django.db.models import F

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def index(request):
    return HttpResponse("Hello world")

class Done(generic.TemplateView):
    template_name = 'hunts/done.html'

class Answered(generic.TemplateView):
    template_name = 'hunts/answered.html'

class Right(generic.TemplateView):
    template_name = 'hunts/right.html'

class Wrong(generic.TemplateView):
    template_name = 'hunts/wrong.html'

class HuntView(generic.ListView):
    template_name = 'hunts/index.html'
    context_object_name = 'latest_hunt_list'

    def get_queryset(self):
        return Hunt.objects.all()

class DetailView(generic.DetailView):
    model = Hunt
    template_name = 'hunts/detail.html'

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

#@permission_required('hunts.add_response', login_url="/hunts/")
#@user_is_blog_post_user
def sub(request,hunt_id):
    hunt = get_object_or_404(Hunt, pk=hunt_id)
    stops = hunt.stop_set.all()
    u = request.user.username
    try:
        user = Usrs.objects.get(usr=u)
    except: 
        user = Usrs(usr=u,hunt=hunt)

    ans = Answer.objects.get(pk=request.POST['answer']) #return a type of Answer to ans
    try:
        cor = Corrects.objects.get(usr=user.usr,correct=ans.text)
        #uco = Corrects.objects.get(usrs=user)
        x = 0
    except:
        cor = Corrects(correct=ans.text,usr=user.usr)
        x = 1

    if ans.is_correct and (x==1):
        user.correct_answers+=1
        #cor.usrs = user
        #cor.correct = ans
        user.save()
        cor.save()
        if (user.correct_answers<5): 
            return HttpResponseRedirect('/hunts/right/')
        else:
            return HttpResponseRedirect('/hunts/done/')
    elif ans.is_correct and (x==0):
        return HttpResponseRedirect('/hunts/answered/')
    else:
        return HttpResponseRedirect('/hunts/wrong/')
    
