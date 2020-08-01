from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Affirmation

import requests





def index(request):
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


def affirmation_save(request):
    form = request.POST.get("affirmation")
    model = Affirmation()
    model.name= form
    model.save()
    
    context={

        "data": Affirmation.objects.all()
    }

    return render(request,"affirmation/affirmation_save.html",context)

        


        







