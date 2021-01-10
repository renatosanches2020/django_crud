from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})


def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})
