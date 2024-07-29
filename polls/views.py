from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Choice, Question
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import F

# Create your views here. My first view I might add :)

def vote(request, question_id):
   question = get_object_or_404(Question, pk=question)
   try:
      selected_choice = question.choice_set.get(pk=request.POST["choice"])
   except (KeyError, Choice.DoesNotExist):
      return render(request, "polls/detail.html" { "question": question, "error_message" "You didn't select a choice.": } )
   else:
      selected_choice.votes = F("votes") + 1
      selected_choice.save()

      return
HttpResponseRedirect(reverse("polls:results", args=(question.id)))



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

