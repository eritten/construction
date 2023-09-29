from django import forms
from .models import Application
import re

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        # excluding form_id and date fields
        exclude = ['form_id', 'date']
    # validation for phone number. which should have country code and 12 digits. the country code should be + followed by 3 digits
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not re.match(r'^\+\d{3}\d{9}$', phone_number):
            raise forms.ValidationError("Phone number should be in the format +123123456789")
        return phone_number
    
    # validation for reference1_phone_number and reference2_phone_number. which should have country code and 12 digits. the country code should be + followed by 3 digits
    def clean_reference1_phone_number(self):
        reference1_phone_number = self.cleaned_data['reference1_phone_number']
        if not re.match(r'^\+\d{3}\d{9}$', reference1_phone_number):
            raise forms.ValidationError("Phone number should be in the format +123123456789")
        return reference1_phone_number
    
    def clean_reference2_phone_number(self):
        reference2_phone_number = self.cleaned_data['reference2_phone_number']
        if not re.match(r'^\+\d{3}\d{9}$', reference2_phone_number):
            raise forms.ValidationError("Phone number should be in the format +123123456789")
        return reference2_phone_number
    
    # validate dates_employed  and end_date. end_date should be greater than dates_employed
    def clean_end_date(self):
        dates_employed = self.cleaned_data['dates_employed']
        end_date = self.cleaned_data['end_date']
        if end_date < dates_employed:
            raise forms.ValidationError("End date should be greater than dates employed")
        return end_date