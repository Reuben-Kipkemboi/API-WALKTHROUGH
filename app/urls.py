from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.next, name='next'),
    path('api/students/', views.StudentsList.as_view(), name='studentendpoint'),
    path('api/students/student-id/<pk>',
        views.StudentsDescription.as_view())
    
]
   
