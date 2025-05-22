from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company_name', 'job_role', 'location', 'salary','experience', 'job_description', 'responsibilities', 'requirements', 'about_company']
        widgets = {
            'company_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Company name'}),
            'job_role' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter job role'}),
            'location' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
            'salary' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter salary package'}),
            'experience' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter required experience'}),
            'job_description' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter job description'}),
            'responsibilities' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter responsiblities'}),
            'requirements' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter job description'}),
            'about_company' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter about Company'}),


        }
            
        