from django import forms
from .models import Profile, Fruit


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {'first_name': forms.TextInput(attrs={'placeholder': "First Name"}, ),
                   'last_name': forms.TextInput(attrs={'placeholder': "Last Name"}, ),
                   'email': forms.TextInput(attrs={'placeholder': "Email"}, ),
                   'password': forms.PasswordInput(attrs={'placeholder': 'Password',})
                   }
        labels ={
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }


class FruitCreationForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'placeholder': "Fruit Name"}, ),
                   'image': forms.TextInput(attrs={'placeholder': "Fruit Image URL"}, ),
                   'description': forms.TextInput(attrs={'placeholder': "Fruit Description"}, ),
                   'nutrition': forms.TextInput(attrs={'placeholder': 'Nutrition Info',})
                   }
        labels = {
            'name': '',
            'image': '',
            'description': '',
            'nutrition': '',
        }


class FruitEditForm(FruitCreationForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'placeholder': "Fruit Name"}, ),
                   'image': forms.TextInput(attrs={'placeholder': "Fruit Image URL"}, ),
                   'description': forms.TextInput(attrs={'placeholder': "Fruit Description"}, ),
                   'nutrition': forms.TextInput(attrs={'placeholder': 'Nutrition Info',})
                   }
    labels = {
        'name': 'Name:',
        'image': "Image URL:",
        'description': "Description:",
        'nutrition': "Nutrition:"
    }


class FruitDeleteForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image', 'description']
        labels = {
            'name': 'Name:',
            'image': "Image URL:",
            'description': "Description:"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image', 'age']
        labels = {
            'first_name': 'First Name:',
            'last_name': "Last Name:",
            'image': "Image URL:",
            'age': "Age:"
        }
