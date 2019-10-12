from tasklister.models import *
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"