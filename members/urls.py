from .views import *
from django.urls import path

urlpatterns = [
    path('signup/',UserRegisterView.as_view(),name='signup'),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
    
]