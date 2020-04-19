from django import forms
from .models import Report

class DateInput(forms.DateInput):
    input_type = 'date'
    

class ReportForm(forms.ModelForm):
    
    class Meta:
        widgets = {'date':DateInput()}
        model=Report
        fields='__all__'
        labels={
            "TL":"Team Leads",
            "No_hours":"No. of Hours",
            "Progress":"Today's Progress",
            "Dtoday":"Upload Today's Documents",
            "concern":"Concern if any",
            "Nextplan":"Next Plan",
            "Dnextp":"Upload Next Plan Documents If Any"
        }
        
