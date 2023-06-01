from django.urls import path
from .views import *

app_name="blog"

urlpatterns = [
    path('listblog/',   ListaBlogListView.as_view(), name="listablog"),
    path('createblog/', CrearBlogCreateView.as_view(), name="crearblog"),
    path('<int:pk>/', DetalleBlogDetailView.as_view(), name="detalleblog"),
    path('<int:pk>/editblog/', EditarBlogUpdateView.as_view(), name="editarblog"),
    path('<int:pk>/delete/', EliminarBlogDeleteView.as_view(), name="eliminar")

]
