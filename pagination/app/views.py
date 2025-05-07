from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Book,Product
from .serializers import BookSerializer,ProductSerializer
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination


# we can also built a custom pagination class
# class custompagination(PageNumberPagination):
#     page_size=10
#     page_size_query_param='page_size'
#     max_page_size=100

# using built-in
class BookListView(ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    # pagination_class=custompagination

    def list(self,request,*args,**kwargs):

        queryset=self.filter_queryset(self.get_queryset())

        page=self.paginate_queryset(queryset)
        if page is not None:
            serializer=self.get_serializer(page,many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer=self.get_serializer(queryset,many=True)
        return Response(serializer.data)


# class ProductListCreate(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     pagination_class=PageNumberPagination


# class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class BookListView(GenericAPIView):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer

#     def get(self,request):
#         books=self.get_queryset()
#         serializer=self.get_serializer(books,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer)
    
# class BookDetailView(GenericAPIView):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer

#     def get_object(self,request,pk):
#         try:
#             return Book.objects.get(request,pk=pk)
#         except Book.DoesNotExist:
#             raise ValueError("not exists")
        
#     def get(self,request,pk):
#         b=self.get_object(request,pk=pk)
#         serializer=BookSerializer(b)
#         return Response(serializer.data)

#     def put(self,request,pk):
#         b=self.get_object(pk=pk)
#         serializer=BookSerializer(b,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#     def delete(self,request,pk):
#         # b=self.get_object(pk)
#         b=Book.objects.get(pk)
#         b.delete()
#         return Response("Deleted")



# GENERIC VIEWS USING MIXINS:: THis views inherit from genericapiview+mixins

# class ProductListCreateView(ListModelMixin,CreateModelMixin,GenericAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer

#     def get(self,request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)







