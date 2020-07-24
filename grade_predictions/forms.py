
from django.contrib.auth.forms import UserCreationForm
from .models import Student
from django import forms


class StudentSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Student
        fields = ('enrolment_year', 'student_code', 'email')


class StudentLoginForm(forms.Form):
    student_code = forms.IntegerField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

