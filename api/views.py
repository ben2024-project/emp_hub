from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from myapp.models import Employee

from api.serializers import EmployeeSerializer

class EmployeeListCreateView(APIView):
    
    
    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all()

        serializer_instance=EmployeeSerializer(qs,many=True) #SERIALIZATION

        # logic for returning all MEmployee

        return Response(data=serializer_instance.data)


    def post(self,request,*args,**kwargs):
        
        # logic for creating a new Employee
        
        serializer_instance=EmployeeSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:
            
            return Response(data=serializer_instance.errors)
            
        
    
class EmployeeRetriveUpdateDestroy(APIView):

     def get(self,request,*args,**kwargs):
        
         id=kwargs.get("pk")

         Movie_obj=Employee.objects.get(id=id) 

         serializer_instance=EmployeeSerializer(Movie_obj,many=False)  #DESERIALIZATION

         # logic for returning Employee detail

         return Response(data=serializer_instance.data)
     
     def put(self,request,*args,**kwargs):
        
        # logic for updating a Employee  
        
        id=kwargs.get("pk")

        Movie_obj=Employee.objects.get(id=id) 

        serializer_instance=EmployeeSerializer(data=request.data,instance=Movie_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:
            
            return Response(data=serializer_instance.errors)
             
     def delete(self,request,*args,**kwargs):

        # logic for deleting a Employee

        id=kwargs.get("pk")

        Employee.objects.get(id=id).delete()

        return Response(data={"message":"employee deleted"})
     

class DepartmentsView(APIView):
    
    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all().values_list("department",flat=True).distinct()

        return Response(data=qs)


class LocationView(APIView):
    
    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all().values_list("location",flat=True).distinct()

        return Response(data=qs)






 
    
    