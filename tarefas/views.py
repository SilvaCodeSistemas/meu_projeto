from django.shortcuts import render

from django.http import  HttpResponse


def lista_tarefas(request):
    tarefas = ['Estudar Django', 'Fazer exercícios', 'Ler documentação']
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})