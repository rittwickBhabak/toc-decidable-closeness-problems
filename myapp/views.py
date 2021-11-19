from django.shortcuts import redirect, render
from myapp.models import Language, Decidiability, Problem, IsClosed, SetOperation, DecidiabilityNote, ClosurePropertyNote
from django.urls import reverse
import random

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
        'decidiability_notes': DecidiabilityNote.objects.all(),
        'closureproperty_notes': ClosurePropertyNote.objects.all(),
    })

def quiz(request):
    languages = Language.objects.all()
    problems = Problem.objects.all()
    set_operations = SetOperation.objects.all()
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
        # object.save()
        return redirect(reverse('myapp:table-page'))

def toggle_decidiability(request, pk):
    if request.method=='POST':
        object = Decidiability.objects.filter(pk=pk)[0]
        object.is_decidiable = not object.is_decidiable
        # object.save()
        return redirect(reverse('myapp:table-page'))

def tough_quiz(request):
    languages = Language.objects.all()
    problems = Problem.objects.all()
    set_operations = SetOperation.objects.all()
    decidiabilities = Decidiability.objects.all()
    closeness = IsClosed.objects.all()

    question_list = []

    langs = random.sample(set(languages), 3)
    probs = random.sample(set(problems), 3)
    ops = random.sample(set(set_operations), 3)

    for lang in langs:
        for prob in probs:
            p = Decidiability.objects.filter(language=lang, problem=prob)[0]
            question = f"Is <u>{prob.title}</u> problem of <u>{lang.title}</u> is decidiable?"
            if p.is_decidiable:
                answer = f"<u>{prob.title}</u> problem of <u>{lang.title}</u> is DECIDABLE."
            else:
                answer = f"<u>{prob.title}</u> problem of <u>{lang.title}</u> is NOT DECIDABLE."
            question_list.append({'question': question, 'answer': answer})

    for lang in langs:
        for op in ops:
            p = IsClosed.objects.filter(language=lang, set_operation=op)[0]
            question = f"Is <u>{lang.title}</u> closed under <u>{op.title}</u>?"
            if p.is_closed:
                answer = f"<u>{lang.title}</u> closed under <u>{op.title}</u>."
            else:
                answer = f"<u>{lang.title}</u> NOT closed under <u>{op.title}</u>."
            question_list.append({'question': question, 'answer': answer})
    random.shuffle(question_list)
    return render(request, 'myapp/quiz2.html', {'question_list': question_list})


def add_note_dec(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        DecidiabilityNote.objects.create(text=text)
        return redirect(reverse('myapp:table-page'))

def add_note_cp(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        ClosurePropertyNote.objects.create(text=text)
        return redirect(reverse('myapp:table-page'))