from django.shortcuts import redirect

def home(request) :
    response = redirect('/rental/')
    return response

