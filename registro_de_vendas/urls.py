from django.urls import path
from registro_de_vendas import views

urlpatterns = [
    path('', views.index, name='index'),
    path('consulta-registro/', views.consulta_registro, name='consulta_registro'),
    path('consulta-registro/<int:pk>', views.registro_detalhado, name='registro_detalhado'),
]