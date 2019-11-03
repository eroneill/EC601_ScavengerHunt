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
	s = True

	for stop in stops:
		ans = stop.answer_set.all()
		try:
			ans = stop.answer_set.get(pk=request.POST['answer'])	#KeyError pops out with this line.
																	#I've tried few thing within bracket such as
																	#'answer{{ answer.text }}' or even something with Stop
																	#lmk if any of you have a clue. I am looking into QueryDict
																	#which might help.
																	#Also checking files under templates
		except(KeyError,Answer.DoesNotExist):
			return render(request,'hunts/detail.html',{
				'hunt':hunt,
				'error_message':"You didn't select a choice.",
				})
		else:
			s = s and ans.is_correct
	if s:
		return HttpResponse('Congrats! You did it!')
	return HttpResponse('Almost there... Keep going!')
