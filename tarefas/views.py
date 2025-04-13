from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from tarefas.models import Tarefa


def listar_tarefas(request):
    '''
    '''
    print(f"Request : {request}")
    tarefas = Tarefa.objects.all().order_by("-criada_em")
    return render(request, template_name="tarefas/listar.html", context={"tarefas":tarefas})


def criar_tarefa(request):
    '''
    '''
    if request.method == "POST":
        print("AAAAA")
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")

        print(f"\t>>{titulo} - {descricao}")
        if titulo:
            Tarefa.objects.create(titulo=titulo, descricao=descricao)
        return redirect("listar_tarefas")
    
    return render(request=request, template_name="tarefas/criar.html")


def concluir_tarefa(request, id):
    '''
    '''
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.concluida = True
    tarefa.save()

    return redirect("listar_tarefas")


def excluir_tarefa(request, id):
    '''
    '''
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('listar_tarefas')