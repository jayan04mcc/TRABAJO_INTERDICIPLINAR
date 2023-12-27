from django.urls import path
from . import views

urlpatterns =[
   
    path('index2/',views.view_index2, name='red_index2'),
    path('usuario/',views.usuario),
    path('puntaje/',views.resultados),
    path('', views.registro_view, name='registro' ),
    path('index1/',views.view_index1, name='red_index1'),
    path('indexprueba/',views.indexprueba)
]
