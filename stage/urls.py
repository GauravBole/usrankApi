
from django.urls import path
from .views import StageApiView,StageListApiView, UserStageApiView, UserStageListApiView
urlpatterns = [
	path('stage/', StageListApiView.as_view(), name="stage"),
	path('stage/<int:pk>/', StageApiView.as_view(), name="stage_detail" ),
	path('user_stage/', UserStageListApiView.as_view(), name="user_stage"),
	path('user_stage/<int:pk>/', UserStageApiView.as_view(), name="user_stage" )
]