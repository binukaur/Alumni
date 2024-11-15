#By this we can convert all the data into JSON.

from rest_framework import serializers
from api.models import AlumniInfo, AlumniPhone, AcademicHistory, Achievements, ProfessionalHistory, SocialMedia

# Serializer for AlumniInfo
class AlumniInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #alumni_id = serializers.ReadOnlyField()  if we want to expose alumni id. By ReadOnlyField(), we cannot update id.
        model = AlumniInfo
        fields = "__all__" # Include fields as per requirements.If you want to use all fields then just write "__all__".

# Serializer for AlumniPhone
class AlumniPhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #id = serializers.ReadOnlyField()  if we want to expose alumni id. By ReadOnlyField(), we cannot update id.
        model = AlumniPhone
        fields = "__all__" # Include fields as per requirements.If you want to use all fields then just write "__all__".

# Serializer for AcademicHistory
class AcademicHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #id = serializers.ReadOnlyField()  if we want to expose alumni id. By ReadOnlyField(), we cannot update id.
        model = AcademicHistory
        fields = "__all__" # Include fields as per requirements.If you want to use all fields then just write "__all__".

# Serializer for Achievements
class AchievementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #id = serializers.ReadOnlyField()  if we want to expose alumni id. By ReadOnlyField(), we cannot update id.
        model = Achievements
        fields = "__all__" # Include fields as per requirements.If you want to use all fields then just write "__all__".

# Serializer for ProfessionalHistory
class ProfessionalHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #id = serializers.ReadOnlyField()  if we want to expose alumni id. By ReadOnlyField(), we cannot update id.
        model = ProfessionalHistory
        fields = "__all__" # Include fields as per requirements.If you want to use all fields then just write "__all__".

# Serializer for SocialMedia
class SocialMediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #id = serializers.ReadOnlyField()  if we want to expose alumni id. By ReadOnlyField(), we cannot update id.
        model = SocialMedia
        fields = "__all__" # Include fields as per requirements.If you want to use all fields then just write "__all__".
