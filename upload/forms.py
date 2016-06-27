from django import forms

class UploadFileForm(forms.Form):
    email_id = forms.EmailField(required=True)
    file = forms.FileField(required=True)
    fallout_report=forms.BooleanField(required=False)
