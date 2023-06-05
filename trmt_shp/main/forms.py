from .models import Order, User
from django.forms import ModelForm, TextInput, PasswordInput


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone']

    widgets = {
        "name": TextInput(attrs={
            'class': 'input_place',
            'name': 'name',
            'placeholder': 'Name',
            'data-max-length': "20",
            'data-min-length': "2",
            'id': "1"
        }),
        "email": TextInput(attrs={
            'class': 'input_place',
            'name': 'email',
            'placeholder': 'Email',
            'data-max-length': "50",
            'data-min-length': "6",
            'id': "2"
        }),
        "phone": TextInput(attrs={
            'class': 'input_place',
            'name': 'phone',
            'placeholder': 'Phone',
            'data-max-length': "20",
            'data-min-length': "9",
            'id': "3"
        })
    }
 
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'password']

        widgets = {
            "nickname": TextInput(attrs={
                'class': 'input_place',
                'name': "nickname",
                'placeholder': "Nickname",
                'data-max-length': "20",
                'data-min-length': "4",
                'id': "1"
            }),
            "password": PasswordInput(attrs={
                'class': 'input_place',
                'name': "pass",
                'placeholder': "Password",
                'data-max-length': "20",
                'data-min-length': "6",
                'id': "2"
            }),
        }
