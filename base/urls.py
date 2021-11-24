
from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
   path('login/', views.CustomloginView.as_view(), name='login'),
   path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
   path('register/', views.RegisterView.as_view(), name='register'),

   
   
   path('', views.TaskList.as_view(),name="tasks"),
   path('task/<int:pk>/', views.TaskDetail.as_view(),name="task"),
   path('task-craet/', views.TaskCreate.as_view(),name="task-craet"),
   path('task-update/<int:pk>/', views.TaskUpdate.as_view(),name="task-update"),
   path('task-delete/<int:pk>/', views.TaskDelete.as_view(),name="task-delete"),

]

