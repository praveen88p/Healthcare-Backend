from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PatientViewSet,
    DoctorViewSet,
    RegisterView,
    LoginView,
    PatientDoctorMappingViewSet,
)

router = DefaultRouter()
router.register("patients", PatientViewSet, basename="patients")
router.register("doctors", DoctorViewSet, basename="doctors")
router.register("mappings", PatientDoctorMappingViewSet, basename="mappings")  
app_name = "api"
urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),  
    path("auth/login/", LoginView.as_view(), name="login"), 
    path("api/", include(router.urls)),  
]
