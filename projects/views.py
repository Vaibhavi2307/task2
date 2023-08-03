from django.shortcuts import render
from .serializers import ProjectSerializer
from .models import Projects
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import logging
logger=logging.getLogger('django')


class ProjectAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=Projects.objects.all()
        serializer=ProjectSerializer(data,many=True)
        print(serializer.data)
        return Response(data=serializer.data)
    
    def post(self,request):
        serializer=ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("project info is posted")
            return Response(data=serializer.data)
        else:
            logger.debug('This is debug')
      
        return Response(data=serializer.errors)
    
class ProjectsDetails(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk=None):
        obj=get_object_or_404(Projects,pk=pk)
        serializer=ProjectSerializer(obj)
        return Response(data=serializer.data)
    
    def put(self,request,pk=None):
        obj=get_object_or_404(Projects,pk=pk)
        serializer=ProjectSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            logger.info("project info is updated")
            return Response(data=serializer.data)
        else:
            logger.debug('This is debug')
       
        return Response(data=serializer.errors)
    
    def patch(self,request,pk=None):
        obj=get_object_or_404(Projects,pk=pk)
        serializer=ProjectSerializer(data=request.data,instance=obj,partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("project info is updated")
            return Response(data=serializer.data)
        else:
            logger.debug('This is debug')
           
        return Response(data=serializer.errors)
    
    def delete(self,request,pk=None):
        obj=get_object_or_404(Projects,pk=pk)
        obj.delete()
        logger.info("record deleted succesfully")
        return Response(data=None)

