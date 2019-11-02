from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import HuntClue, ClueAnswer, Hunt, Stop, Answer, Response, Usrs

#def index(request):
#	return HttpResponse("Hello world")


class IndexView(generic.ListView):
	template_name = 'hunts/index.html'
	context_object_name = 'latest_hunts_list'

class DetailView(generic.DetailView):
	model = Hunt
	template_name = 'hunts/detail.html'

class ResultView(generic.DetailView):
	model = Hunt
	template_name = 'hunts/detail.html'

def more(request, hunt_id):	#see stops
	hunt = get_object_or_404(Hunt, pk=hunt_id)
	stops = hunt.stop_set.get(pk=hunt_id)
	
def check(request, stop_id):
	stop = get_object_or_404(stop,pk=stop_id)
	try:
		selected_answer = stop.answer_set.get(pk=request.POST['answer'])
	except(KeyError, Answer.DoesNotExist):
		return render(request,'hunt/detail.html',{
			'error_message':"You haven't completed the hunt.",
			})
	else:
		selected_answer.save()
		return HttpResponseRedirect(reverse('hunts:results',args=(hunt.slug,))) 

