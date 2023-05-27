from django.urls import path
from .views import *

app_name="blog"

urlpatterns = [
    path('listblog/', BlogListView.as_view(), name="listadblog"),
    path('crearblog/', CrearBlogListView.as_view(), name="crarblog")
]
