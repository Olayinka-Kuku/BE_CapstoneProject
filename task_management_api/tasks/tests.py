from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task
from .serializers import TaskSerializer

class TaskSerializerTestCase(TestCase):
    
    def setUp(self):
        # Set up a user (required for task assignments)
        self.user = get_user_model().objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)  # Authenticate the client with this user
        
        # Create a sample task for testing
        self.task = Task.objects.create(
            title="Sample Task",
            description="This is a sample task",
            due_date="2025-01-10",
            user=self.user
        )
    
    def test_task_serializer(self):
        """Test the Task serializer to make sure it works correctly"""
        task_data = TaskSerializer(self.task).data
        self.assertEqual(task_data['title'], "Sample Task")
        self.assertEqual(task_data['description'], "This is a sample task")
        self.assertEqual(str(task_data['due_date']), "2025-01-10")
        self.assertEqual(task_data['user'], self.user.id)  # Ensure the user ID is correctly serialized
        
    def test_task_list_api(self):
        """Test the Task API endpoint to make sure it's working"""
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if the task created earlier appears in the response data
        task_data = response.data
        self.assertEqual(len(task_data), 1)  # Only one task should be returned
        self.assertEqual(task_data[0]['title'], "Sample Task")
        self.assertEqual(task_data[0]['description'], "This is a sample task")
