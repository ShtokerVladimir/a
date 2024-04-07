from django import forms
from django.core.exceptions import ValidationError

# class RegisterForm(forms.ModelForm):
#   class Meta:
#     model = User
#     fields = ['username', 'email', 'password', 'confirm_password']
  
#   def cleanUsername(self):
#     username = self.cleaned_data['username']
#     if User.objects.filter(username=username).exists():
#       raise ValidationError('Username already exists')
#     return username

#   def cleanEmail(self):
#     email = self.cleaned_data.get('email')
#     if User.objects.filter(email=email).exists():
#       raise ValidationError('Email is not valid')
#     return email
  
#   def cleanPassword(self):
#     password = self.cleaned_data['password']
#     confirm_password = self.cleaned_data['confirm_password']
#     if len(password) < 6:
#       raise ValidationError('Password cannot be less than 6 characters!')
#     elif password.isalpha() or password.isnumeric():
#       raise ValidationError('Password should contains at least one letter and one number!')
#     elif password != confirm_password:
#       raise ValidationError('Passwords do not match!')
#     return password

class LoginForm(forms.Form):
  username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput)
  password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)

CHOICES = {
  "text/csv": "CSV",
  "text/tab-separated-values": "TSV",
  "text/plain": "TXT",
  "application/json": "JSON",
}  

class FileForm(forms.Form):
  file = forms.FileField(label="File", widget=forms.FileInput, required=False)
  type = forms.ChoiceField(required=True, choices=CHOICES)
  
class BirthdayGreeterForm(forms.Form):
  name = forms.CharField(label="Name", max_length=50, widget=forms.TextInput)
  text = forms.CharField(label="Text", max_length=50, widget=forms.TextInput)