from django.http import HttpResponse, HttpRequest

def greetings(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World!")