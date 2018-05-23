from django.shortcuts import render
from .forms import ContactForm, SnippetForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name, email)

    form = ContactForm()
    return render(request, 'myapp/form.html', {'form': form})


def snippet_detail(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            print('Valid')


    form = SnippetForm()
    return render(request, 'myapp/form.html', {'form': form})