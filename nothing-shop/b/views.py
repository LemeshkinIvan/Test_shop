from django.shortcuts import render, redirect
from .forms import SubscribersForm


def create(request):
    error =''
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('a')
        else:
            error = 'error'

    form = SubscribersForm()
    data = {'form': form,
            'error': error,
            }

    return render(request, 'b/b_page.html', data)
