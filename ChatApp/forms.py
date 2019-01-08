from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'repeat_password'
                  )
        widgets = {'password': forms.PasswordInput}

        def clean(self):
            cleaned_data = super().clean()

            field1 = cleaned_data.get('password')
            field2 = cleaned_data.get('repeat_password')

            username = cleaned_data.get('username')
            email = cleaned_data.get('email')
            if User.objects.filter(username=username).exist():
                self.add_error("username", "Username already occupied")

            if User.objects.filter(email=email).exists():
                self.add_error("email", "User with this email already exist")

            if field1 != field2:
                self.add_error("repeat_password", "Password and repeat_password should be the same")
