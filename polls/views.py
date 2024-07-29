from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Choice, Question
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import F
from django.views import generic

# Create your views here. My first view I might add :)

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    # same as above, no changes needed.
    ...
















'''
def vote(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   try:
      selected_choice = question.choice_set.get(pk=request.POST["choice"])
   except (KeyError, Choice.DoesNotExist):
      return render(request, "polls/detail.html", {"question": question, "error_message": "You didn't select a choice."})
   else:
      selected_choice.votes = F("votes") + 1
      selected_choice.save()

      # always return an httpresponseredirect after successfully dealing with POST data.
      #This prevents data from being posted twice if a user hits the Back button.
      #its good web dev practice apparently. 

      return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



def index(request):
   return HttpResponse("Greetings human, you have arrived at my polls site.")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})



def result(request, question_id):
   response = "You're looking at the results of question %s."
   return HttpResponse(response, question_id)

def vote(request, question_id):
   return HttpResponse("You're voting on question %s. % question_id")

def index(request):
   latest_question_list = Question.objects.order_by("pub_date")[:5]
   
   context = {
      "latest_question_list": latest_question_list
   }
   return render(request, "polls/index.html", context)

def results(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(request, "polls/results.html", {"question": question})'''







class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    # same as above, no changes needed.
    ...