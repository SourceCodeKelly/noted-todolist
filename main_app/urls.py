from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

# this like app.use() in express
urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('', views.TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetails.as_view(), name='task'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
    path('task-edit/<int:pk>/', views.TaskEdit.as_view(), name='task-edit'),
    path('task-delete/<int:pk>/', views.TaskDelete.as_view(), name='task-delete'),
]