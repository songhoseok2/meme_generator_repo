from django.urls import path
from . import views

urlpatterns = [
    path('/<text>/<font_size>/<font_red>/<font_green>/<font_blue>/<farm>/<server_id>/<photo>', views.display_final_result, name='input_keyword_path_name'),
]

