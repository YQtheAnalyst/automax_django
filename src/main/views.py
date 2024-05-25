from django.shortcuts import render

from django.http import HttpResponse


def main_view(request):

    # return HttpResponse("<h1>Welcome to Automax!</h1>")
    return render(request, "views/main.html", {"name": "Automax"})

