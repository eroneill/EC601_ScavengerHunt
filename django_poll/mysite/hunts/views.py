from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import HuntClue, ClueAnswer, Hunt, Stop, Answer, Response, Usrs

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


def sub(request,hunt_id):
    hunt = get_object_or_404(Hunt, pk=hunt_id)
    stops = hunt.stop_set.all()
    
    ans = Answer.objects.get(pk=request.POST['answer']) 
    if ans.is_correct:
        return HttpResponse('Congrats! You did it!')
    else:
        return HttpResponse('Almost there... Keep going!')
    