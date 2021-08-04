from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string



def index(request):
    palabras = get_random_string(length=14)
    context = {
        "pala" : palabras
    }

    if 'contador' in request.session:
        request.session['contador'] = request.session['contador'] + 1
    else:
        request.session['contador'] = 1
    return render(request, 'index.html',context)



def reset(request):
    request.session['contador'] = 0
    return redirect('/')




