from django import forms

class LoginForm(forms.Form):
  username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput)
  password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)
  
class FileForm(forms.Form):
  file = forms.FileField(label="File", widget=forms.ClearableFileInput, required=True, max_length=100, allow_empty_file=False)