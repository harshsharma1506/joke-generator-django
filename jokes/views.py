from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
import pyjokes 

# views contains the logic that is behind the things happening on the front end 
#models contains all the logical structure for the database 

def main(request):
   jokes=[]
   for x in range(5):
       jokes.append(pyjokes.get_joke())
   context={
       'jokes':jokes,
   }
   return render(request,'index.html',context)
