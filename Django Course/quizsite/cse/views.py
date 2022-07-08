
from django.http.request import validate_host
from django.shortcuts import render
from .models import *
def index(request):
    return render(request,"index.html")

def test(request):
  return render(request,"test.html")
already_done=[]
qno=0
def about(request):
  global qno
  import pandas as pd
  import random
  df=pd.read_csv(r"E:\My Codes\Django Course\quizsite\cse\static\csv\newquizdata.csv")
  mylist=random.sample(range(0,3),3)
  for item in mylist: 
    if item not in already_done:   
      Question=df.Question[item]
      Option_A=df.Option_A[item]
      Option_B=df.Option_B[item]
      Option_C=df.Option_C[item]
      Option_D=df.Option_D[item]
      Answer=df.Answer[item]   

      radio1=request.POST.get("options-outlined1")
      radio2=request.POST.get("options-outlined2")
      radio3=request.POST.get("options-outlined3")
      radio4=request.POST.get("options-outlined4")
      Submit_Click=request.POST.get("mysubmit")


      if Answer==radio1:
        pass
      elif Answer==radio2:
        pass
      elif Answer==radio3:
        pass
      else:
        pass
      print(radio1)
      print(radio2)
      print(radio3)
      print(radio4)
      print(Submit_Click)
      qno+=1
      params={
            "Question":Question,
            "Option_A":Option_A,
            "Option_B":Option_B,
            "Option_C":Option_C,
            "Option_D":Option_D,
            "Answer":Answer,
            "Qno":qno,
            }    
      already_done.append(item)
      return render(request,"about.html",params)
    else:
      continue
  return render(request,"finish.html")
   

