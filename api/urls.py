from django.contrib import admin
from django.urls import path,include
from api.views import AlumniInfoViewSet,AlumniPhoneViewSet, AcademicHistoryViewSet, AchievementsViewSet, ProfessionalHistoryViewSet, SocialMediaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alumni', AlumniInfoViewSet)
router.register(r'phone', AlumniPhoneViewSet)
router.register(r'academic-history', AcademicHistoryViewSet)
router.register(r'achievements', AchievementsViewSet)
router.register(r'professional-history', ProfessionalHistoryViewSet)
router.register(r'social-media', SocialMediaViewSet)


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',include(router.urls))


   
]