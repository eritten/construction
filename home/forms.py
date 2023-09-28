from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        # excluding form_id and date fields
        exclude = ['form_id', 'date']