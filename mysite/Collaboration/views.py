from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class CollaborationAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        data = request.data.copy()
        data['Admin'] = request.user.username
        serializer = CollaborationSerializer(data = data)
        obj = Collaboration.objects.all()
        getserializer=CollaborationSerializer(obj,many = True)
        if not serializer.is_valid():
            return Response({
                'status': 400,
                'message':serializer.errors,
                'data': serializer.data
            },status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response({
                'status': 201,
                'message':'Collaboration Created Successfully',
                'instance': serializer.data,
                'data': getserializer.data
            },status.HTTP_201_CREATED)
        
    def get(self,request):
        data = Collaboration.objects.all()
        serializer = CollaborationSerializer(data,many = True)
        return Response({
            'status':200,
            'data':serializer.data,
            'message':'Fetch Successful'
        },status.HTTP_200_OK)
    
    def delete(self,request):
        data = request.data.copy()
        data['Admin'] = request.user.username
        if data['CollabName']:
            instance = Collaboration.objects.filter(CollabName = data['CollabName'],Admin = data['Admin'])
            if instance:
                instance.delete()
                obj = Collaboration.objects.all()
                serializer = CollaborationSerializer(obj,many=True)
                return Response({
                    'status': 200,
                    'message' : 'Collaboration Deleted Successfully',
                    'data' :  serializer.data
                },status.HTTP_200_OK)
            else:
                return Response({
                    'status':400,
                    'message':'Not Allowed'
                },status.HTTP_400_BAD_REQUEST)
        else :
            return Response({
                'status':400,
                'message':'CollabName is Required'
            },status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request):
        data = request.data
        instance = Collaboration.objects.get(id = data['id'])
        if not instance.Admin == request.user.username:
            return Response({
                'status':400,
                'message':'Not Allowed'
            },status.HTTP_400_BAD_REQUEST)
        serializer = CollaborationSerializer(instance,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':200,
                'message':'Update Successful',
                'instance': serializer.data
            },status.HTTP_200_OK)
        else:
            return Response({
                'status':400,
                'message':serializer.errors,
                'instance': serializer.data
            },status.HTTP_400_BAD_REQUEST)


class CollabMembersAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post (self ,request):
        data = request.data.copy()
        data['CollabMembers'] = request.user.username
        serializer = CollabMembersSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status':400,
                'message':serializer.errors,
                'instance':serializer.data
            },status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response({
                'status':201,
                'message' : 'Member Added Successfully',
                'instance': serializer.data
            })
        
    def get(self,request):
        data = request.data
        if data['type'] =='Collab':
            obj = CollabMembers.objects.filter(CollabName=data['CollabName'])
        else:
            obj = CollabMembers.objects.filter(CollabMembers=request.user.username)
        
        serializer = CollabMembersSerializer(obj,many=True)
        return Response({
            'status':200,
            'message':'Fetch Successful',
            'instance':data,
            'data':serializer.data
        },status.HTTP_200_OK)
    
    def delete(self,request):
        data = request.data
        Instance = Collaboration.objects.get(id=data['CollabName'])
        if request.user.username ==  Instance.Admin :
            instance = CollabMembers.objects.get(CollabName=data['CollabName'],CollabMembers = data['CollabMembers'])
            instance.delete()
            return Response({
                'status': 200,
                'message':'Member Deleted Successfully',
                'instance':data
            },status.HTTP_200_OK)
        else:
            instance = CollabMembers.objects.get(CollabName=data['CollabName'],CollabMember = request.user.username)
            instance.delete()
            return Response({
                'status':200,
                'message':'Left The Collaboration Successfully',
                'instance':data
            },status.HTTP_200_OK)
    
    def patch(self, request):
        data = request.data
        instances = CollabMembers.objects.filter(CollabMembers = request.user.username)
        print(instances)
        for instance in instances:
            instance.CollabMembers = data['new_username']
            instance.save()
        return Response({
            'status':200,
            'message':'Collab Members Updated',
            'instance':data
        },status.HTTP_200_OK)
    

class CollabDataAPI(APIView):
    permission_classes =[IsAuthenticated]
    # parser_classes = (MultiPartParser,FormParser)

    def post(self,request):
        data = request.data.copy()
        data['MemberName'] = request.user.username
        serializer = CollabDataSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status':400,
                'message':serializer.errors,
                'intance':serializer.data
            },status.HTTP_400_BAD_REQUEST)
        else:
            try:
                serializer.save()
                obj = CollabData.objects.all()
                getserializer = CollabDataSerializer(obj,many=True)
            except UnicodeDecodeError:
                return Response({
                    'status':200,
                    'message':'Instance Created Successfully',
                    'instance':data,
                    # 'data':getserializer.data
                },status.HTTP_200_OK)
            else:
                # obj = CollabData.objects.all()
                # getserializer = CollabDataSerializer(obj,many=True)
                return Response({
                    'status':200,
                    'message':'Instance Created Successfully',
                    'instance':data,
                    'data':getserializer.data
                },status.HTTP_200_OK)