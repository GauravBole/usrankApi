from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.db import models

# Create your models here.
User = get_user_model()

class Stage(models.Model):
	"""docstring for Stage"""
	question = models.CharField(max_length=100, null=False, blank=False)
	
	@property
	def userStage(self):
		return self.userstage_set.all().values().order_by('-point','time')
		# return self.question
	

class UserStage(models.Model):
	"""docstring for UserStage"""

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	stage = models.ForeignKey(Stage,on_delete=models.CASCADE)
	answer = models.CharField(max_length=100, blank=True, null=True)
	point = models.IntegerField(default=0)
	time = models.IntegerField(default=0)

	def __str__(self):
		return self.user.user_id

	
# This is optional part 
def pre_save_user_point(sender, instance, *args, **kwargs):
	user_obj = User.objects.get(user_id=instance.user.user_id)

	if not instance.id:

		user_obj.time_spend = user_obj.time_spend + instance.time
		user_obj.point = user_obj.point + instance.point
		user_obj.save()
	else:
		previous = UserStage.objects.get(id=instance.id)
		user_obj.time_spend = user_obj.time_spend - previous.time
		user_obj.point = user_obj.point + previous.point
		user_obj.save()
		if user_obj.time_spend < 0:
			user_obj.time_spend = 0 + instance.time
		else:
			user_obj.time_spend = user_obj.time_spend + instance.time
		if user_obj.point < 0:
			user_obj.point = 0 + instance.point
		else:
			user_obj.point = user_obj.point + instance.point

		user_obj.save()


	
pre_save.connect(pre_save_user_point,sender=UserStage)
		