from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy
from .models import Docente
from .models import NoDocente
from .forms import DocenteForm
from .forms import NoDocenteForm


# Create your views here.



class DocenteListViewAll(ListView):
    model = Docente 
    template_name = "registrodoc/list_all.html"
    ordering = 'last_name'
    context_objet_name = 'lista'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.getc('kword','')
        lista = Docente.objects.filter(
            last_name__icontains = palabra_clave
        )
        return lista


class NoDocenteListViewAll(ListView):
    model = NoDocente 
    template_name = "registrodoc/list_all2.html"
    ordering = 'last_name'
    context_objet_name = 'lista'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.getc('kword','')
        lista = NoDocente.objects.filter(
            last_name__icontains = palabra_clave
        )
        return lista        





class DocenteListViewBuscar(ListView):
    model = Docente
    template_name = "registrodoc/buscar.html"
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave = self.request.GET.getc('kword','')
        lista = Docente.objects.filter(
            last_name = palabra_clave
        )
        return lista

class NoDocenteListViewBuscar(ListView):
    model = NoDocente
    template_name = "registrodoc/buscar2.html"
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave = self.request.GET.getc('kword','')
        lista = NoDocente.objects.filter(
            last_name = palabra_clave
        )
        return lista
    

class DocenteDetailView(DetailView):
    model = Docente
    template_name = "registrodoc/detalle.html"
    context_object_name = 'detalle'

class NoDocenteDetailView(DetailView):
    model = NoDocente
    template_name = "registrodoc/detalle2.html"
    context_object_name = 'detalle'    


class SuccesView(TemplateView):
    template_name = "registrodoc/exito.html"


class DocenteCreateView(CreateView):
    model = Docente
    template_name = "registrodoc/alta.html"
    form_class = DocenteForm
    success_url = reverse_lazy('registrodoc.app:listar-todo')

    def form_valid(self, form):
        docente = form.save(commit = False)
        docente.full_name = docente.first_name + ' ' + docente.last_name
        docente.save()
        return super(DocenteCreateView, self).form_valid(form)


class NoDocenteCreateView(CreateView):
    model = Docente
    template_name = "registrodoc/alta2.html"
    form_class = NoDocenteForm
    success_url = reverse_lazy('registrodoc.app:listar-todo2')

    def form_valid(self, form):
        nodocente = form.save(commit = False)
        nodocente.full_name = nodocente.first_name + ' ' + nodocente.last_name
        nodocente.save()
        return super(NoDocenteCreateView, self).form_valid(form)



class DocenteUpdateView(UpdateView):
    model = Docente
    template_name = "registrodoc/update.html"
    form_class = DocenteForm
    Success_url = reverse_lazy('registrodoc_app:listar-todo') 

    def form_valid(self, form):
        docente = form.save(commit = False)
        docente.full_name = docente.first_name + ' ' + docente.last_name
        docente.save()
        return super(DocenteUpdateView, self).form_valid(form)

class NoDocenteUpdateView(UpdateView):
    model = NoDocente
    template_name = "registrodoc/update2.html"
    form_class = NoDocenteForm
    Success_url = reverse_lazy('registrodoc_app:listar-todo2') 

    def form_valid(self, form):
        nodocente = form.save(commit = False)
        nodocente.full_name = nodocente.first_name + ' ' + nodocente.last_name
        nodocente.save()
        return super(NoDocenteUpdateView, self).form_valid(form)




class DocenteDeleteView(DeleteView):
    model = Docente
    template_name = "registrodoc/delete.html"
    success_url = reverse_lazy('registrodoc_app:listar-todo') 

class NoDocenteDeleteView(DeleteView):
    model = NoDocente
    template_name = "registrodoc/delete2.html"
    success_url = reverse_lazy('registrodoc_app:listar-todo2') 


class VistaPrincipal(TemplateView):
    template_name = "index.html"
