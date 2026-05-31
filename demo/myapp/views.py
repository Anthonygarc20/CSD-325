from django.http import HttpResponse

def index(request):
    return HttpResponse("Garcia says Hello!")
