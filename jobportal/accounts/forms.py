from django import forms
from django.contrib.auth.models import User
from .models import Job
from .models import Application

class JobForm(forms.ModelForm):

    class Meta:
        model = Job

        fields = [
            'title',
            'company',
            'location',
            'salary',
            'experience',
            'job_type',
            'description',
            'skills',
            'deadline'
        ]

class SignupForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'email',
            'password'
        ]

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Passwords do not match."
            )

        return cleaned_data
    
class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application

        fields = [
            'candidate_name',
            'email',
            'phone',
            'education',
            'skills',
            'resume',
            'cover_letter'
        ]