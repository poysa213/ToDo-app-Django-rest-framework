from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('tasks/', views.taskList, name="task-list"),
    path('tasks/<str:pk>/', views.taskDetail, name="task-Detail"),
    path('tasks/', views.taskCreate, name="task-Create"),
    path('tasks/<str:pk>/', views.taskUpdate, name="task-update"),
    path('tasks/<str:pk>/', views.taskDelete, name="task-delete"),
]