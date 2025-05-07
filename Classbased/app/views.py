from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status


class StudentlistView(APIView):

    def get(self,request):
        st=Student.objects.all()
        serializer=StudentSerializer(st,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class Studentupdate(APIView):

    def get_object(self,request,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return None
        
    def get(self,request,pk):
        st=self.get_object(pk=pk)
        serializer=StudentSerializer(st)
        return Response(serializer.data)
    
    def put(self,request,pk):
        st=self.get_object(pk=pk)
        serializer=StudentSerializer(st,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self,request,pk):
        st=Student.objects.get(pk=pk)
        st.delete()
        return Response("deleted")