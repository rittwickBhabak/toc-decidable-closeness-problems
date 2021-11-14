from django.shortcuts import redirect, render
from myapp.models import Language, Decidiability, Problem, IsClosed, SetOperation
from django.urls import reverse

def tables(request):
    languages = Language.objects.all()
    set_operations = SetOperation.objects.all()
    problems = Problem.objects.all()
    decidiabilities = Decidiability.objects.all()
    closeness = IsClosed.objects.all()

    decidiability_table = []
    closeness_table = []

    for problem in problems:
        temp_list = [problem.title]
        for language in languages:
            is_decidiable = Decidiability.objects.filter(language=language, problem=problem)[0]
            temp_list.append(is_decidiable)
        decidiability_table.append(temp_list)


    for set_operation in set_operations:
        temp_list = [set_operation.title]
        for language in languages:
            is_closed = IsClosed.objects.filter(language=language, set_operation=set_operation)[0]
            temp_list.append(is_closed)
        closeness_table.append(temp_list)

    return render(request, 'myapp/tables.html', {
        'languages': languages,
        'set_operations': set_operations,
        'problems': problems,
        'decidiabilities': decidiabilities,
        'closeness': closeness,
        'decidiability_table': decidiability_table,
        'closeness_table': closeness_table,
    })

def quiz(request):
    languages = Language.objects.all()
    set_operations = SetOperation.objects.all()
    problems = Problem.objects.all()
    decidiabilities = Decidiability.objects.all()
    closeness = IsClosed.objects.all()

    decidiability_table = []
    closeness_table = []

    for problem in problems:
        temp_list = [problem.title]
        for language in languages:
            is_decidiable = Decidiability.objects.filter(language=language, problem=problem)[0]
            temp_list.append(is_decidiable)
        decidiability_table.append(temp_list)


    for set_operation in set_operations:
        temp_list = [set_operation.title]
        for language in languages:
            is_closed = IsClosed.objects.filter(language=language, set_operation=set_operation)[0]
            temp_list.append(is_closed)
        closeness_table.append(temp_list)

    return render(request, 'myapp/quiz.html', {
        'languages': languages,
        'set_operations': set_operations,
        'problems': problems,
        'decidiabilities': decidiabilities,
        'closeness': closeness,
        'decidiability_table': decidiability_table,
        'closeness_table': closeness_table,
    })
   

def toggle_closeness(request, pk):
    if request.method=='POST':
        object = IsClosed.objects.filter(pk=pk)[0]
        object.is_closed = not object.is_closed 
        object.save()
        return redirect(reverse('myapp:table-page'))

def toggle_decidiability(request, pk):
    if request.method=='POST':
        object = Decidiability.objects.filter(pk=pk)[0]
        object.is_decidiable = not object.is_decidiable
        object.save()
        return redirect(reverse('myapp:table-page'))
