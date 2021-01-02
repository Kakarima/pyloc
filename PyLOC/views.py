from django.shortcuts import redirect


def home(request):
    response = redirect('/rental/')
    return response


def gestion(request):
    response = redirect('/gestion/')
    return response
