from django.shortcuts import render
from django.http import HttpResponse

def start(request):
    return HttpResponse('<h1>First veiw</h1>')
