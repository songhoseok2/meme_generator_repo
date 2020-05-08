from django.urls import path
from . import views

urlpatterns = [
    path('/<text>/<farm>/<server_id>/<photo>', views.display_final_result, name='input_keyword_path_name'),
]

