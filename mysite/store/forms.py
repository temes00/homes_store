import re
from django import forms
from django.forms import ModelForm
from .models import Order

PHONE_MASK = r'[+][7][\s]{0,1}[\(]{0,1}\d{3}[\)]{0,1}[\s]{0,1}\d{3}[\-]{0,1}\d{2}[\-]{0,1}\d{2}'
EMAIL_MASK = r'.*\@.*\..*'


class OrderCreateForm(ModelForm):
    def clean(self):
        cleaned_data = super(OrderCreateForm, self).clean()
        name = cleaned_data.get('name')
        lastname = cleaned_data.get('lastname')
        phone = cleaned_data.get('phone')
        email = cleaned_data.get('email')

        if not name or not lastname:
            raise forms.ValidationError((
                'Please fill in both fields (Name,LastName).'
            ))
        if not phone or not email:
            raise forms.ValidationError((
                'Please fill in both fields (PhoneNumber,Email).'
            ))
        if not re.match(PHONE_MASK, phone):
            raise forms.ValidationError((
                'You enter invalid phone number!'
            ))
        if not re.match(EMAIL_MASK, email):
            raise forms.ValidationError((
                'You enter invalid email!'
            ))
        return cleaned_data

    class Meta:
        model = Order
        fields = ('name', 'lastname', 'phone', 'email', 'comment')
