from django.shortcuts import render
from rest_framework import viewsets
from api.models import AlumniInfo, AlumniPhone, AcademicHistory, Achievements, ProfessionalHistory, SocialMedia
from api.serializers import AlumniInfoSerializer, AlumniPhoneSerializer, AcademicHistorySerializer, AchievementsSerializer, ProfessionalHistorySerializer, SocialMediaSerializer

# Create your views here.

class AlumniInfoViewSet(viewsets.ModelViewSet):      #Except CRUD, if we need any functionality then we can write here.
    queryset = AlumniInfo.objects.all()
    serializer_class = AlumniInfoSerializer

class AlumniPhoneViewSet(viewsets.ModelViewSet):
    queryset = AlumniPhone.objects.all()
    serializer_class = AlumniPhoneSerializer

class AcademicHistoryViewSet(viewsets.ModelViewSet):
    queryset = AcademicHistory.objects.all()
    serializer_class = AcademicHistorySerializer

class AchievementsViewSet(viewsets.ModelViewSet):
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer

class ProfessionalHistoryViewSet(viewsets.ModelViewSet):
    queryset = ProfessionalHistory.objects.all()
    serializer_class = ProfessionalHistorySerializer

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
