from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-details'),
    
]