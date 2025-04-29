from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Product.objects.values_list('category', flat=True).distinct(),
        empty_label="Select",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'stock', 'description', 'image']
