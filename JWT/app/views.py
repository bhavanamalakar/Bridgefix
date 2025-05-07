from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProfileView(APIView):
    permission_classes=[IsAuthenticated]  #only accessible if logged in

    def get(self,request):
        user=request.user
        data={
            'username':user.username,
            'email': user.email,
        }
        return Response(data)
    

