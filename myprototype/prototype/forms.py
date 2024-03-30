from django import forms

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