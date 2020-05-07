from django.urls import path
from . import views

urlpatterns = [
    path('', views.ask_keyword, name='input_keyword_path_name'),
]

