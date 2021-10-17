from django.urls import path
from . import views

urlpatterns = [
    path('topics/', views.getTopics),
    path('topics/<str:pk>/', views.getTopic),
]
