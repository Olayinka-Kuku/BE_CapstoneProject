from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('users/', views.UserCreateView.as_view(), name='user-create'),
    path('token/', views.get_auth_token, name='get-token'),
]