from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='estoque'),
    path('', views.EstoqueView.as_view(), name='estoque'),
    
]