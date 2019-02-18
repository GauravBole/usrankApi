from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Stage, UserStage
User = get_user_model()

class StageSerializer(serializers.ModelSerializer):
	"""docstring for AuthUserSerializers"""
	users = serializers.SerializerMethodField()
	class Meta:
		model = Stage
		fields = "__all__"

	def get_users(self, obj):
		user_data = obj.userStage
		
		return user_data

class StageUserSerializer(serializers.ModelSerializer):
	"""docstring for AuthUserSerializers"""
	Q = serializers.HyperlinkedIdentityField(
        view_name="stage:stage_detail",
        lookup_field="pk"
    )
	class Meta:
		model = UserStage
		fields = '__all__'


# class UserRank(serializers.ModelSerializer):
# 	"""docstring for UserRank"""
	
# 	class Meta:
# 		model = UserStage
# 		fields = '__all__'

