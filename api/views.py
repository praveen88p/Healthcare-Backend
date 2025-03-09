from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import (
    DoctorSerializer,
    UserSerializer,
    PatientSerializer,
    PatientDoctorMappingSerializer,
)


# User Registration View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


# User Login View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
class LoginView(generics.GenericAPIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = User.objects.get(email=email)  
        except User.DoesNotExist:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=user.username, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({"refresh": str(refresh), "access": str(refresh.access_token)})

        return Response({"error": "Incorrect password"}, status=status.HTTP_400_BAD_REQUEST)

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  


# Doctor Management ViewSet
class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_superuser:  # Only admins can add doctors
            return Response({"error": "Only admins can add doctors"}, status=status.HTTP_403_FORBIDDEN)
        serializer.save(user=self.request.user)


# Patient-Doctor Mapping ViewSet
class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.all()

    def perform_create(self, serializer):
        serializer.save()
