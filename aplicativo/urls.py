from django.urls import path, include
from . import views
urlpatterns = [
    path('acessar_curso/', views.mudar_mensagem)
]