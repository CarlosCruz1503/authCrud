from .models import *
from django.forms import ModelForm, DateInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ('date_complete',"user")
        widgets={'date_for_complete': DateInput(attrs={'type':"date"})}