from django.urls import path
from .views import *

urlpatterns = [
    path('', PropertyView.as_view()),
    path('item/<str:type>/', SelectedPropertyView.as_view()),
    path('<str:type>/<int:id>/', PropertyDetailView.as_view()),
    path('create/<str:type>/', CreateProperty.as_view()),
    path('delete/<str:type>/<int:pk>/', DeleteProperty.as_view()),
    path('thisuser/', UserPropertyView.as_view()),
]