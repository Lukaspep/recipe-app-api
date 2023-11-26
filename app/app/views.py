from django.shortcuts import render, redirect

def redirect_to_swagger(request):
    return redirect('/api/docs')

def default_view(request):
    return render(request, 'index.html')
