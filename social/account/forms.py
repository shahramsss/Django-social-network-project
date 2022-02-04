import django


from django import forms


class RegisterAccountForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password_1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
