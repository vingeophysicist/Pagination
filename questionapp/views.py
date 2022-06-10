from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Question


def index(request):
   questions = Question.objects.all().order_by('-publish')
   paginator = Paginator(questions, 5) # 5 question per page
   page = request.GET.get('page', 1)
   try:
      questions = paginator.get_page(page)
   except PageNotAnInteger:
      questions = paginator.get_page(1)
   except EmptyPage:
      questions = paginator.get_page(paginator.num_pages)
    
   
   context = {"questions":questions}
   return render(request, "index.html", context)


                                                                                                                    
                                                                                                                    
                                                                                                                    
                                                                                                                    
                                                                                                                    
                                                                                                                    