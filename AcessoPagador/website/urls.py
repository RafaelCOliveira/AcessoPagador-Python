# Importamos a função index() definida no arquivo views.py
from . import views
from django.urls import path

app_name = 'website'

# urlpatterns a lista de roteamentos de URLs para funções/Views
urlpatterns = [
    # GET /
    #path(r'^$', views.Pagamento),
    path('Pagamento', views.Pagamento),
    path('Visualizar/<id>', views.Visualizar),
    path('Capturar/<id>', views.Capturar),
    path('Cancelar/<id>', views.Cancelar),
    path('Pagar', views.Pagar),
    
]