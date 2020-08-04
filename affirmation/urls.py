from django.urls import path
from . import views

urlpatterns = [
    path('affirmation/', views.index, name='affirmation_home'),
    path('affirmation_display/',views.AffirmationView.as_view(), name='affirmation-view'),
    path('affirmation_save/',views.AffirmationSave, name='affirmation_save'),
    path('create_affirmation/',views.AffirmationCreate.as_view(), name='create_affirmation'),
    # path('delete_affirmation/<str:pk>',views.deleteAffirmaiton, name='delete_affirmation')
]
