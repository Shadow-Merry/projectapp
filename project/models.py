from django.db import models

# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status

class Priority(models.Model):
    priority = models.CharField(max_length=200)

    def __str__(self):
        return self.priority

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=200)
    updated_date = models.DateTimeField(auto_now=True)
    priority = models.ForeignKey(Priority, on_delete = models.SET_NULL, null= True)
    status = models.ForeignKey(Status, on_delete = models.SET_NULL, null =True)

    def __str__(self):
        return self.project_name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete =models.CASCADE)
    task_name = models.CharField(max_length=200)
    task_description = models.TextField(null=True, blank=True)
    assigned_to = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete = models.SET_NULL, null= True)
    status = models.ForeignKey(Status, on_delete = models.SET_NULL, null=True)
    

    def __str__(self):
        return self.task_name


class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete= models.CASCADE)
    assigned_to = models.CharField(max_length=200)
    subtask_name= models.CharField(max_length=200)
    subtask_description = models.TextField(null= True, blank=False)
    assigned_by = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete = models.SET_NULL, null= True)
    status = models.ForeignKey(Status, on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return self.subtask_name

