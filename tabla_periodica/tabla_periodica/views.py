from django.shortcuts import render

def tabla(request):
    return render(request, 'tabla/tabla.html')