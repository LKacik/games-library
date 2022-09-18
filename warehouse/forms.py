from .models import AddGame
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = AddGame
        fields = '__all__'
