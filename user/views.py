from django.http import HttpResponse

def user_home(requests, *args, **kwargs):
    return HttpResponse("<h1>Hello</h1>")