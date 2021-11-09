from django.forms import ModelForm
from .models import Project , Task , SubTask

class CreateProject(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class CreateTask(ModelForm):
    class Meta:
        model= Task
        fields = '__all__'

class CreateSubtask(ModelForm):
    class Meta:
        model = SubTask
        fields = '__all__'