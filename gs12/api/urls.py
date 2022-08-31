from django.urls import path
from api import views

urlpatterns = [
    path('stucreate/', views.StudentListCreateAPI.as_view()),
    path('stucreate/<int:pk>', views.StudentRetrieveUpdateDestroyAPI.as_view()),

    # path('stucreate/<int:pk>', views.StudentList.as_view()),
]