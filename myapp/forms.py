from django import forms


class EmployeeForm(forms.Form):

    name=forms.CharField()

    department=forms.CharField()

    salary=forms.IntegerField()
    
    location=forms.CharField()

    email=forms.CharField()

    address=forms.CharField()