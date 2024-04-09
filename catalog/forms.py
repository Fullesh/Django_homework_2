from django import forms

from catalog.models import Product, Version


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('updated_by',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        if cleaned_data in ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'):
            raise forms.ValidationError('У-пс, название товара в списке запрещённых товаров')

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        exclude = ('product', 'version_number', 'name_of_version', 'actual_version_indicator')
