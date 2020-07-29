from django.urls import path
from . import views

urlpatterns = [
    path('affirmation/', views.index, name='affirmation_home'),
]
