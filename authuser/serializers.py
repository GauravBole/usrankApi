from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models import Sum
from rest_framework import serializers
from stage.models import UserStage
import random
User = get_user_model()

def create_userid(new_code = None):
    "Genrate randome number to avoid dublicate of user name or email id"
    random_id = random.randint(0, 9999999)
    user_code = str(random_id)
    if new_code is not None:
        user_code = new_code
    qs = User.objects.filter(user_id = user_code)
    if qs.exists():
        user_code = str(random_id)

        return create_usercode(new_code=user_code)
    return user_code
    
class AuthUserSerializers(serializers.ModelSerializer):
	"""docstring for AuthUserSerializers"""
	user = serializers.SerializerMethodField()
	
	class Meta:
		model = User
		fields = ("name","email", "password", "user_id", 'user')
		extra_kwargs = {
            'usercode': {
                'validators': [UnicodeUsernameValidator()],
                'read_only': True
            	},
            }

	def get_user(self, obj):
		# user_rank = obj.userrank # not excecute due to model manager changed(BaseUser, and normal Manager)
		g = UserStage.objects.filter(user=obj).values().aggregate(Sum('point'), Sum('time'))
		return g
		
	def create(self, validated_data):
		user_code = create_userid()
		obj , user = User.objects.get_or_create(user_id = user_code)
		obj.name = validated_data['name']
		obj.email = validated_data['email']
		obj.set_password(validated_data['password'])
		obj.save()
		return obj

	def update(self, instance, validated_data):
		obj = User.objects.get(id=instance.id)
		obj.name = validated_data['name']
		obj.email = validated_data['email']
		obj.set_password(validated_data['password'])
		obj.save()
		return obj

		
