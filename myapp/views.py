from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View

from myapp.models import Employee

from myapp.forms import EmployeeForm


class EmployeeListView(View):

    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all()

        return render(request,"employeelist.html",{"data":qs})
    
class EmployeeCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=EmployeeForm()

        return render(request,"Employeecreate.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Employee.objects.create(**data) 

            return redirect("employee-list")
        else:

            return render(request,"employeecreate.html",{"form":form_instance})
        
class EmployeeDetailView(View):

     def get(self,request,*args,**kwargs):
         
         id=kwargs.get("pk")

         qs=Employee.objects.get(id=id)

         return render(request,"employeedetail.html",{"data":qs})    
     

class EmployeeDeleteView(View):     

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Employee.objects.get(id=id).delete()

        return redirect("employee-list")
    

class EmployeeEditView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        emp_object=Employee.objects.get(id=id) 

        dictionary={
            "name":emp_object.name,
            "department":emp_object.department,
            "salary":emp_object.salary,
            "location":emp_object.location,
            "email":emp_object.email,
            "address":emp_object.address
        }

        form_instance=EmployeeForm(initial=dictionary)

        return render(request,"employee_edit.html",{"form":form_instance})   


    def post(self,request,*args,**kwargs):

        from_instance=EmployeeForm(request.POST)

        id=kwargs.get("pk")

        if from_instance.is_valid():

            data=from_instance.cleaned_data

            Employee.objects.filter(id=id).update(**data)

            return redirect("employee-list")
        
        else:

            return render(request,"employee_edit.html",{"form":from_instance})     