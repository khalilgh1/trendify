from django.forms import ModelForm, TextInput, Textarea, NumberInput, FileInput, Select
from .models import Product

class productForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write a description...',
                'rows': 4
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price'
            }),
            'image': FileInput(attrs={
                'class': 'form-control-file'
            }),
            'language': Select(attrs={
                'class': 'form-select'
            }),
            'category': Select(attrs={
                'class': 'form-select'
            }),
        }