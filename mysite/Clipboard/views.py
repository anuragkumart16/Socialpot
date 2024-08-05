from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LinkSerializers ,TextSerializers ,FileSerializers, AnotherTextSerializers, AnotherFileSerializers, AnotherLinkSerializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
    
class linkhandler(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data
        serializer = LinkSerializers(data=data)
        if not serializer.is_valid():
            return Response({
                'status' : 400,
                'message':'Bad request, invaild Item given',
                'details':serializer.errors
            },status.HTTP_400_BAD_REQUEST)
        print(serializer.data)
        instance = Linkmodel(Link = serializer.data['Link'],user= request.user.username)
        instance.save()
        return Response({
            'status' : 200,
            'message' : 'link Stored Successfully',
        },status.HTTP_200_OK)

    def get(self,request):
        obj = Linkmodel.objects.filter(user=request.user.username)
        serializer = AnotherLinkSerializers(obj,many=True)
        return Response({
            'status':200,
            'message':'Fetch Successful',
            'data':serializer.data
        },status.HTTP_200_OK)
    
    def delete(self,request):
        data = request.data
        instance = Linkmodel.objects.get(id=data['id'])
        instance.delete()
        return Response({
            'status':200,
            'message': 'Link deleted'
        },status.HTTP_200_OK)



class texthandler(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data
        serializer = TextSerializers(data=data)
        if not serializer.is_valid():
            return Response({
                'status' : 400,
                'message':'Bad request, invaild Item given',
            },status.HTTP_400_BAD_REQUEST)

        instance = Textmodel(Text = serializer.data['Text'],user = request.user.username)    
        instance.save()
        return Response({
            'status' : 200,
            'message' : 'Text Stored Successfully',
        },status.HTTP_200_OK)

    def get(self,request):
        obj = Textmodel.objects.filter(user=request.user.username)
        serializer = AnotherTextSerializers(obj,many=True)
        return Response({
            'status':200,
            'message':'Fetch Successful',
            'data':serializer.data
        },status.HTTP_200_OK)
    
    def delete(self,request):
        data = request.data
        instance = Textmodel.objects.get(id=data['id'])
        instance.delete()
        return Response({
            'status':200,
            'message': 'Text deleted'
        },status.HTTP_200_OK)

class filehandler(APIView):
    permission_classes =[IsAuthenticated]
    def post (self,request):
        data = request.data.copy()
        data['user_obj'] = request.user.username
        serializer = FileSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':200,
                'message':'The file is uploaded'
            },status.HTTP_200_OK)
        else:
            return Response({
            'status':400,
            'message':'Invalid Value Entered'
            },status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        data = Filemodel.objects.filter(user_obj=request.user.username)
        serializer = FileSerializers(data , many=True)
        return Response({
            'status':200,
            'message':'fetch Successful',
            'data': serializer.data
        },status.HTTP_200_OK)
    
    def delete(self,request):
        data = request.data
        instance = Filemodel.objects.get(id = data['id'])
        instance.delete()
        return Response({
            'status':200,
            'message': 'Item Deleted'
        },status.HTTP_200_OK)
