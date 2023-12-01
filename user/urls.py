from django.urls import path, include
from . import views

urlpatterns = [
  path('', include('djoser.urls.authtoken')),
	path('me/', views.UserView, name='me'),
  path('edit/', views.EditUserView.as_view()),
]