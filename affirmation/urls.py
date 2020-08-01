from django.urls import path
from . import views

urlpatterns = [
    path('affirmation/', views.index, name='affirmation_home'),
    path('affirmation_display/',views.AffirmationView.as_view(), name='affirmation-view'),
    path('affirmation_save/',views.affirmation_save, name="affirmation_save")
]
