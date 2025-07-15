
from django.contrib import admin
from django.urls import path
from tarefas import views  # importa as views da app tarefas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_tarefas)  # rota principal
]
