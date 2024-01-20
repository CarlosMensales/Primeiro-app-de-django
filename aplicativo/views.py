from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso
from datetime import datetime

#funções vem aqui

def listar_curso(request):
    nome_filtrar = request.GET.get('filtro_nome')
    carga_filtrar = request.GET.get('filtro_carga')

    cursos = Curso.objects.all()
    
    if nome_filtrar:
        cursos = cursos.filter(nome__contains=nome_filtrar)

    if carga_filtrar:
        cursos = cursos.filter(carga_horaria__gte=carga_filtrar)
        

    return render(request, 'listar_curso.html', {'cursos': cursos})
def criar_curso(request):
    if request.method == "GET":
        status = request.GET.get('status')
        return render(request, 'criar_curso.html', {'status': status})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        carga_horaria = request.POST.get('carga_horaria')
        curso = Curso(
            nome = nome,
            carga_horaria = carga_horaria,
            data_de_criacao = datetime.now()
        )

        curso.save()

        return redirect('/curso/criar_curso/?status=1')
def ver_curso(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, 'ver_curso.html', {'curso': curso})
def deletar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.ativo = False
    curso.save()
    return redirect('/curso/listar_curso')
