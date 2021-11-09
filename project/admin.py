from django.contrib import admin
from .models import SubTask,Task,Project,Status,Priority

# Register your models here.
admin.site.register(SubTask)
admin.site.register(Status)
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Priority)