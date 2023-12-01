from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EditUserSerializer, UserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

User = get_user_model()
	
class EditUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = EditUserSerializer(
            data=request.data,
            instance=user,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"ویرایش حساب کاربری با موفقیت انجام شد!"})
        return Response(serializer.errors, status=status.HTTP_409_CONFLICT)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def UserView(request):
    return Response(UserSerializer(request.user).data)