from django.shortcuts import render
from django.http import HttpResponse

#funções vem aqu

def mudar_mensagem(request):
    return HttpResponse('Teste')