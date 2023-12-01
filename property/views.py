from drf_multiple_model.views import FlatMultipleModelAPIView
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class PropertyView(FlatMultipleModelAPIView):
    querylist = [{'queryset': Home.objects.all(), 'serializer_class': HomeSerializer},
                 {'queryset': Car.objects.all(), 'serializer_class': CarSerializer},
                 {'queryset': Other.objects.all(), 'serializer_class': OtherSerializer}]
    
class SelectedPropertyView(FlatMultipleModelAPIView):
    def get_querylist(self):
        type = self.kwargs.get('type')
        if type :
            if type == 'home' :
                return [{'queryset':Home.objects.all(), 'serializer_class': HomeSerializer}]
            elif type == 'car' :
                return [{'queryset':Car.objects.all(), 'serializer_class': CarSerializer}]
            elif type == 'other' :
                return [{'queryset':Other.objects.all(), 'serializer_class': OtherSerializer}]
            else:
                return ValueError('تایپ نامشخص!')
    

class PropertyDetailView(FlatMultipleModelAPIView):
    def get_querylist(self):
        type = self.kwargs.get('type')
        id = self.kwargs.get('id')
        if type and id :
            if type == 'home' :
                return [{'queryset':Home.objects.filter(id=id), 'serializer_class': HomeDetailSerializer}]
            elif type == 'car' :
                return [{'queryset':Car.objects.filter(id=id), 'serializer_class': CarDetailSerializer}]
            elif type == 'other' :
                return [{'queryset':Other.objects.filter(id=id), 'serializer_class': OtherDetailSerializer}]
            else:
                return ValueError('تایپ نامشخص!')


class UserPropertyView(FlatMultipleModelAPIView):
    permission_classes = [IsAuthenticated]
    def get_querylist(self):
        user = self.request.user
        querylist = [{'queryset': Home.objects.filter(author=user), 'serializer_class': HomeSerializer},
                    {'queryset': Car.objects.filter(author=user), 'serializer_class': CarSerializer},
                    {'queryset': Other.objects.filter(author=user), 'serializer_class': OtherSerializer}]
        return querylist
    
class CreateProperty(CreateAPIView):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        type = self.kwargs['type']
        if type == 'home' :
            serializer_class = HomeDetailSerializer
            return Home.objects.all()
        elif type == 'car' :
            serializer_class = CarDetailSerializer
            return Car.objects.all()
        elif type == 'other' :
            serializer_class = OtherDetailSerializer
            return Other.objects.all()
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_create(instance)
        return HttpResponse(status=status.HTTP_201_CREATED)
    
class DeleteProperty(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        type = self.kwargs['type']
        pk = self.kwargs['pk']
        if type and pk :
            if type == 'home' :
                serializer_class = HomeDetailSerializer
                return Home.objects.filter(author=user, id=pk)
            elif type == 'car' :
                serializer_class = CarDetailSerializer
                return Car.objects.filter(author=user, id=pk)
            elif type == 'other' :
                serializer_class = OtherDetailSerializer
                return Other.objects.filter(author=user, id=pk)
            else:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return HttpResponse(status=status.HTTP_200_OK)