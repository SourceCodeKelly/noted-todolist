from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.taskList, name='tasks')
]