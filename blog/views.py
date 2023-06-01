from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView


from .models import Post
from .forms import PostCrearForm

# Create your views here.

class ListaBlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()

        context = {
            'posts':posts
        }
        return render(request, 'BlogList.html', context)
    
class CrearBlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PostCrearForm()

        context ={
            'form':form
        }
        return render(request, 'CrearBlog.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form = PostCrearForm(request.POST)
            if form.is_valid():
                titulo = form.cleaned_data.get('titulo')
                contenido = form.cleaned_data.get('contenido')

                p, created = Post.objects.get_or_create(titulo=titulo, contenido=contenido)
                p.save()

                return redirect('blog:listablog')

        context = {
        }
        return render(request, 'CrearBlog.html', context)
    


class DetalleBlogDetailView(View):

    def get(self, request, pk, *args, **kwargs):
        listaPost = get_object_or_404(Post, pk=pk)

        context ={
            'listaPost':listaPost

        }
        return render(request, 'DetalleBlog.html', context)
    

class EditarBlogUpdateView(UpdateView):
    model=Post
    fields=['titulo', 'contenido']
    template_name='EditarBlog.html'

    def get_success_url(self):
        pk=self.kwargs['pk']
        return reverse_lazy('blog:detalleblog', kwargs={'pk':pk})
    

class EliminarBlogDeleteView(DeleteView):
    model=Post
    template_name='EliminarBlog.html'
    success_url=reverse_lazy('blog:listablog')