import logging
from rest_framework import status,generics
logger = logging.getLogger(__name__)
from .serializers import CreateUserSerializer, TestSerializer, ResultSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from .models import Test,User



class RegisterView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        logger.debug(f"Request data: {request.data}")
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            logger.error(f"Errors: {response.data}")
        return response
class TestView(APIView):
    def get(self, request: Request, pk=None,q_type=None,q_subject=None) -> Response:
        if pk is None and q_subject is None and q_type is None:
            tests = Test.objects.all()
            serializer = TestSerializer(tests, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif q_subject==None and q_type==None:
            try:
                test = Test.objects.get(pk=pk)
                serializer = TestSerializer(test)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Test.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif pk==None and q_subject==None:
            try:
                test = Test.objects.filter(question_type1=q_type)
                serializer = TestSerializer(test,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Test.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif pk==None:
            try:
                task = Test.objects.filter(question_type1=q_type,question_subject=q_subject)
                serializer = TestSerializer(task,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Test.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
