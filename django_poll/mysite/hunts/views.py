from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
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

@permission_required('hunts.add_response', login_url="/hunts/")
#@user_is_blog_post_user
def sub(request,hunt_id):
    hunt = get_object_or_404(Hunt, pk=hunt_id)
    stops = hunt.stop_set.all()
    u = request.user.username
    try:
        user = Usrs.objects.get(usr=u)
    except: 
        user = Usrs(usr=u,hunt=hunt)

    ans = Answer.objects.get(pk=request.POST['answer'])
    try:
        cor = Corrects.objects.get(usrs=user,correct=ans)
        #uco = Corrects.objects.get(usrs=user)
        x = 0
    except:
        cor = Corrects(correct=ans,usrs=user)
        x = 1

    if ans.is_correct and (x==1):
        user.correct_answers+=1
        #cor.usrs = user
        #cor.correct = ans
        user.save()
        cor.save()
        return HttpResponse(cor.usrs)
        #return HttpResponse('Congrats! You did it!')
    if ans.is_correct and (x==0):
        return HttpResponse('Unfortunately, you already answered this question. Your points are unchanged')
    else:
        return HttpResponse('Almost there... Keep going!')
    
