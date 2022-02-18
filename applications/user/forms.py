from django import forms
from .models import User


class UserCreateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("__all__")

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        ),
    )

    full_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    role = forms.ChoiceField(
        required=True,
        choices=User.ROLE_CHOICES,
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    gender = forms.ChoiceField(
        required=True,
        choices=User.GENDER_CHOICES,
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}
        )
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    def clean(self):
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("repeat_password")
        if len(password) < 5:
            self.add_error(
                "password", "Password length must be greater than 5 characters"
            )
            return

        if password != repeat_password:
            self.add_error(
                "repeat_password", "Password and Repeat password are not the same"
            )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'full_name', 'role',
                  'gender', 'date_of_birth', 'is_active')

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        ),
    )

    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    gender = forms.ChoiceField(
        choices=User.GENDER_CHOICES,
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={'class': 'form-control'}
        )
    )
