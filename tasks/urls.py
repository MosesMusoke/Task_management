from django.urls import path
from .views import TaskListCreateView, TaskDetailView, MarkTaskCompleteView, MarkTaskIncompleteView, UserListView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/complete/', MarkTaskCompleteView.as_view(), name='mark-task-complete'),
    path('tasks/<int:pk>/incomplete/', MarkTaskIncompleteView.as_view(), name='mark-task-incomplete'),
    path('users/', UserListView.as_view(), name='user-list'),
]
