#GenericAPIView and Model Mixin
from . models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.mixins import DestroyModelMixin

# Create your views here

#To GET data and POST data
class StudentListCreateAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    #To GET data
    def get(self, request, *args, **kwargs): # for ListModelMixin
        print('\n<<<<<<<<<<<<<<<<GET>>>>>>>>>>>>>>')
        return self.list(request, *args, **kwargs)

    #To POST data
    def post(self, request, *args, **kwargs): # For CreateModelMixin
        print('\n<<<<<<<<<<<<<<<<POST>>>>>>>>>>>>>>')
        return self.create(request, *args, **kwargs)


#To GET(specific data), PUT data, DELETE data
class StudentRetrieveUpdateDestroyAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    #To GET specific data
    def get(self, request, *args, **kwargs):
        print('\n<<<<<<<<<<<<<<<<GET(Specific)>>>>>>>>>>>>>>')
        return self.retrieve(request, *args, **kwargs)

    #To PUT data
    def put(self, request, *args, **kwargs):
        print('\n<<<<<<<<<<<<<<<<PUT>>>>>>>>>>>>>>')
        return self.update(request, *args, **kwargs)

    #To PATCH data
    def patch(self, request, *args, **kwargs):
        print('\n<<<<<<<<<<<<<<<<PATCH>>>>>>>>>>>>>>')
        return self.partial_update(request, *args, **kwargs)

    #To DELETE data
    def delete(self, request, *args, **kwargs):
        print('\n<<<<<<<<<<<<<<<<DELETE>>>>>>>>>>>>>>')
        return self.destroy(request, *args, **kwargs)






# class StudentRetrieve(GenericAPIView, RetrieveModelMixin): #To GET specific data
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def get(self, request, *args, **kwargs): #we need pk's endpoint of our api
#         return self.retrieve(request, *args, **kwargs) #pk will pass internally in retrieve() method


# class StudentUpdate(GenericAPIView, UpdateModelMixin): #To PUT as well as PATCH data
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs) #pk will pass internally in update() method


# class StudentDestroy(GenericAPIView, DestroyModelMixin): #To DELETE data
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs) #pk will pass internally in destroy() method







# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import status
# # from rest_framework.decorators import api_view
# from rest_framework.views import APIView

# # Create your views here
# class StudentAPI(APIView):
#     def get(self, request, pk=None, format=None): #Initially pk=0
#         print("\n<<<<<<<<<<<<<<<<<<<<<<<<<GET>>>>>>>>>>>>>>>>>>>>>>>>")
#         id=pk
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     def post(self, request, format=None):
#         print("\n<<<<<<<<<<<<<<<<<<<<<<<<<POST>>>>>>>>>>>>>>>>>>>>>>>>")
#         serializer=StudentSerializer(data=request.data) #We have all data in //request.data//
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data inserted successfully!!!'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)



#     def put(self, request, pk, format=None):
#         print("\n<<<<<<<<<<<<<<<<<<<<<<<<<PUT>>>>>>>>>>>>>>>>>>>>>>>>>>")
#         id=pk
#         stu=Student.objects.get(pk=id)
#         serializer=StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data updated successfully!!!'}, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



#     def patch(self, request, pk, format=None):
#         print("\n<<<<<<<<<<<<<<<<<<<<<<<<<PATCH>>>>>>>>>>>>>>>>>>>>>>>>>>")
#         id=pk
#         stu=Student.objects.get(pk=id)
#         serializer=StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data updated successfully(partially)!!!'}, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


#     def delete(self, request, pk, fromat=None):
#         print("\n<<<<<<<<<<<<<<<<<<<<<<<<<DELETE>>>>>>>>>>>>>>>>>>>>>>>>>>")
#         id=pk
#         stu=Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg' : 'Data deleted successfully!!!'}, status=status.HTTP_200_OK)
