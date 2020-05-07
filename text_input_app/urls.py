from django.urls import path
from . import views

urlpatterns = [
    path('', views.ask_text, name='input_text_path_name'),
]

