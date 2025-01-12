from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')  # Task owner
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Allow empty descriptions
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    completed_at = models.DateTimeField(null=True, blank=True) # Timestamp for completion
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.title  # Display the task title in the admin

    def save(self, *args, **kwargs):
      if self.status == 'completed' and self.completed_at is None:
        self.completed_at = timezone.now()
      elif self.status == 'pending':
        self.completed_at = None
      super().save(*args, **kwargs)

    class Meta:
      ordering = ['due_date'] #Default ordering