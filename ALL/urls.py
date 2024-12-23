from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.signout, name='logout'),
    path('sign_in/', views.signin, name='signin'),
    path('create/', views.createTask, name='create'),
    path('tasks/', views.showTasks, name='tasks'),
    path('task/<int:task_id>/edit', views.editTask, name='task'),
    path('task/<int:task_id>', views.task, name='taskshow'),
    path('task/<int:task_id>/delete', views.deleteTask, name='delete'),
    path('', views.home, name='home'),

]
