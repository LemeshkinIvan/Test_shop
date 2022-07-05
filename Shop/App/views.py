from django.shortcuts import render, redirect
from .forms import SubscribersForm


def home(request):
    return render(request, 'Home_page/a_page.html')


def send(request):
    error =''
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'error'

    form = SubscribersForm()
    data = {'form': form,
            'error': error,
            }

    return render(request, 'App_page/b_page.html', data)


def contact(request):
    return render(request, 'Contact_page/d_page.html')
