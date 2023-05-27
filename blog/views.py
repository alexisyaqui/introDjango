from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render


from .models import Post
from .forms import PostCrearForm

# Create your views here.

class BlogListView(View):
    def get(self, request, *args, **kwargs):

        context = {
           
        }

        return render(request, 'BlogList.html', context)
    

class CrearBlogListView(View):
    def get(self, request, *args, **kwargs):

        forms = PostCrearForm()

        context ={
            'form':forms

        }

        return render(request, 'CrearBlog.html', context)
    
    def post(self, request, **kwargs):
        
        if request.method=="POST":

        forms = {PostCrearForm(request.POST)}

        context = {
        }
        return render(request, 'CrearBlog.html', context)
    
