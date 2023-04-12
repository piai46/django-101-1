from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'email',
            'featured',
        ]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if 'product' not in name.lower():
            raise forms.ValidationError('This is not a valid name, must contain "product"')
        return name


class RawProductForm(forms.Form):
    name = forms.CharField(max_length=70, label='Product name', widget=forms.TextInput(
        attrs={
            'placeholder': 'name'
        }
    ))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'class': 'new-class two',
                                          'id': 'my-id-for-textarea',
                                          'rows': 12,
                                          'cols': 100,
                                      }
                                  )
                                  )
    price = forms.DecimalField(decimal_places=2)
    email = forms.EmailField(required=False)
    featured = forms.BooleanField(required=False)
