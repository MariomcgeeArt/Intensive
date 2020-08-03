from django.db import models
from django.contrib.auth.models import User



class Affirmation(models.Model):
    name = models.CharField(max_length=200)
  
    user = models.ForeignKey(User, on_delete=models.PROTECT,
                              help_text="The user that posted this article.")
  


