from django.shortcuts import render

def ask_keyword(request):
    return render(request, 'keyword_input_app/keyword_input_page.html')
