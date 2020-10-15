from django.urls import path
from .views import *

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/add', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<pk>', EmployeeEditView.as_view(), name='employee_update_delete'),
    path('employees/details/<pk>', EmployeeDetailsView.as_view(), name='employee_details_list'),
    path('employees/address/<pk>', EmployeeAddressEditView.as_view(), name='employee_address_get_update_delete'),
    path('employees/address/add/<pk>', EmployeeAddressCreateView.as_view(), name='employee_address_create')
]
