from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me_view, name='about_me_view'),
    path('resume/', views.resume_view, name='resume'),
]

