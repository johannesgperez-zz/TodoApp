from django.contrib.auth.views import LogoutView
from django.urls import path

from base.views import (LoginPage, RegisterPage, TaskCreate, TaskDelete,
                        TaskDetail, TaskList, TaskUpdate)

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('task_detail/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('task_create/', TaskCreate.as_view(), name='task_create'),
    path('task_update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task_delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
    
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='base/logout.html'), name='logout'),
    
    path('register/', RegisterPage.as_view(), name='register'),
]
