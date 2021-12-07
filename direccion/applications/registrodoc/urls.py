from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'registrodoc_app'

urlpatterns = [
    path(
        'listar-todo/',
        views.DocenteListViewAll.as_view(),
        name='listar-todo'
    ),
    path(
        'listar-todo2/',
        views.NoDocenteListViewAll.as_view(),
        name='listar-todo2'
    ),   
    path(
        'buscar/',
        views.DocenteListViewBuscar.as_view(),
        name='buscar'
    ),
    path(
        'buscar2/',
        views.NoDocenteListViewBuscar.as_view(),
        name='buscar'
    ),
    path(
        'detalle/<pk>',
        views.DocenteDetailView.as_view(),
        name= 'detalle'
                    
    ),
    path(
        'detalle2/<pk>',
        views.NoDocenteDetailView.as_view(),
        name= 'detalle'
                    
    ),
    path(
        'exito/',
        views.SuccesView.as_view(),
        name='exito'
    ),
    path(
        'alta/',
        views.DocenteCreateView.as_view(),
        name='alta'
    ),
    path(
        'alta2/',
        views.NoDocenteCreateView.as_view(),
        name='alta'
    ),
    path(
        'update/<pk>',
        views.DocenteUpdateView.as_view(),
        name='update'
    ),
    path(
        'update2/<pk>',
        views.NoDocenteUpdateView.as_view(),
        name='update'
    ),
    path(
        'delete/<pk>',
        views.DocenteDeleteView.as_view(),
        name='delete'
    ),
    path(
        'delete2/<pk>',
        views.NoDocenteDeleteView.as_view(),
        name='delete'
    ),
    path(
        '',
        views.VistaPrincipal.as_view(),
        name='index'
    ),
]