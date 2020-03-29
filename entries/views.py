from django.shortcuts import redirect, render

from .forms import EntryForm
from .models import Entry


def index(request):
    entries = Entry.objects.order_by('-date_posted')

    context = {'entries': entries}

    return render(request, 'entries/index.html', context)

def add(request):
    if request.method == 'POST':
        entry_form = EntryForm(request.POST)

        if entry_form.is_valid():
            entry_form.save()

            return redirect('index')
    else:
        entry_form = EntryForm()

    context = {'entry_form': entry_form}

    return render(request, 'entries/add.html', context)
