
from django.urls import path
from .views import AuthUserApiView,AuthUserListApiView
urlpatterns = [
	path('users/', AuthUserListApiView.as_view(), name="users"),
	path('users/<int:pk>/', AuthUserApiView.as_view(), name="users" )

]