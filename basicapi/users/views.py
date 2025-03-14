from django.http import Http404
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import User
from .serializers import UserSerializer

# for creating and listing users
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# for retrieve, update and delete user
class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # override get_object to return message for non-existent user
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound({"error": "Non-existent user"})
        
    #Override destroy method to return succesful message
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)
