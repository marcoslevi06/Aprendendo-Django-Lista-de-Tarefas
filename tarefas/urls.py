from django.urls import path
from tarefas.views import listar_tarefas, criar_tarefa, concluir_tarefa, excluir_tarefa


urlpatterns = [
    path(route="", view=listar_tarefas, name="listar_tarefas"),
    path(route="criar_tarefa", view=criar_tarefa, name="criar_tarefa"),
    path(route="concluir/<int:id>", view=concluir_tarefa, name="concluir_tarefa"),
    path(route="excluir/<int:id>/", view=excluir_tarefa, name="excluir_tarefa"),

]