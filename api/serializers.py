from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping

User = get_user_model()  

class UserSerializer(serializers.ModelSerializer):
    is_doctor = serializers.BooleanField(default=False)  

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "is_doctor"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        is_doctor = validated_data.pop("is_doctor", False)  
        user = User.objects.create_user(**validated_data)
        user.is_doctor = is_doctor 
        user.save()
        return user

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")  
    class Meta:
        model = Patient
        fields = "__all__"

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")  

    class Meta:
        model = Doctor
        fields = "__all__"

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = "__all__"
