from django import forms


from .models import *

class PostCrearForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'