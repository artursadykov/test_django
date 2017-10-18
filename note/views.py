from django.shortcuts import render
from .forms import NoteForms


def note(request):
    name = 'Vasy'
    form = NoteForms (request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(form)
        print(request.POST)
        print(form.cleaned_data)

        new_form = form.save()

    return render(request, 'getdata/getdata.html', locals())
