from django.shortcuts import render


def home(request):
    return render(request, 'a/a_page.html')


# Create your views here.
