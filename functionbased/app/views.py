from rest_framework.decorators import api_view
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response

import logging

logger = logging.getLogger(__name__)

@api_view(['GET','POST'])
def item_list(request):
    if request.method=='GET':
        items=Item.objects.all()
        serializer=ItemSerializer(items,many=True)
        logger.info("item successfullly get")
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=ItemSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        logger.info("item successfullly created")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def item_detail(request,pk):
    try:
        item=Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        logger
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='GET':
        serializer=ItemSerializer(item)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=ItemSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        item.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)



