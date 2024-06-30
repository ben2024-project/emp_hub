from django.urls import path

from api import views

urlpatterns=[

   path('employees/',views.EmployeeListCreateView.as_view()),

   path('employees/<int:pk>/',views.EmployeeRetriveUpdateDestroy.as_view()),

   path('employees/departments/',views.DepartmentsView.as_view()),

   path('employees/locations/',views.LocationView.as_view()),


]


