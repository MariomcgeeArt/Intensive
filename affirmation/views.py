from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Affirmation
from django.views.generic.edit import CreateView
from .forms import AffirmationForm

import requests





def index(request):
   
    print(request.user.username)
    return render(request,'affirmation/affirmation_home.html')


class AffirmationView(ListView):
    def get(self,request):
        url = "https://www.affirmations.dev"

        headers = {
            "Accept": "application/json"
            }
        response = requests.request("GET", url, headers=headers)
        
        context={

            "data": response.json
      


        }
        return render(request,"affirmation/affirmation_display.html",context)


def AffirmationSave(request):
    if request.POST:
            
        form = request.POST.get("affirmation")
        user = request.user
        if user is not None:

            model = Affirmation()
            model.name= form
            model.user = user
            model.save()
        else:
            pass
    else:
        pass
    
        
    context={

        "data": Affirmation.objects.all()
    }
    

    return render(request,"affirmation/affirmation_save.html",context)



class AffirmationCreate(CreateView):

  def get(self, request):
      
      context = {}
      return render(request, 'affirmation/create_affirmation.html', context)

  def post(self, request):
      content = request.post.get('affirmation')
      affriamtaion= Affirmation()
      affirmation.name= content
      affirmaiton.user = request.user
      affirmaiton.save()
   
      return HttpResponseRedirect(reverse_lazy('affirmation_save', args=[affirmation.id]))
     
        


        







