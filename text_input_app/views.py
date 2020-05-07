from django.shortcuts import render

def ask_text(request, keyword):
    return render(request, 'text_input_app/text_input_page.html', {'keyword': keyword})
