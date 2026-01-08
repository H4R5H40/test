from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Django! Local server is working 🚀")