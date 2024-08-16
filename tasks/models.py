from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"Category: {self.name}"

class Task(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='tasks')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-deadline']
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return f"Task: {self.title} (Status: {self.status})"


class SubTask(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['status', 'deadline']
        verbose_name = "SubTask"
        verbose_name_plural = "SubTasks"

    def __str__(self):
        return f"Subtask: {self.title} (Status: {self.status})"
