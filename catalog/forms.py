from django import forms
from .models import Product
from django.core.exceptions import ValidationError

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})  # стилизация
        self.fields['is_available'].widget.attrs.update({'class': 'form-check-input'})  # для чекбокса

    def clean_name(self):
        name = self.cleaned_data['name']
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f"Название не должно содержать запрещённое слово: {word}")
        return name

    def clean_description(self):
        desc = self.cleaned_data['description']
        for word in FORBIDDEN_WORDS:
            if word.lower() in desc.lower():
                raise ValidationError(f"Описание не должно содержать запрещённое слово: {word}")
        return desc

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price
