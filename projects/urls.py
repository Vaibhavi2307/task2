from django.urls import path
from .views import ProjectAPI,ProjectsDetails

urlpatterns=[
    path('projects/',ProjectAPI.as_view()),
    path('projects/<int:pk>/',ProjectsDetails.as_view())
]