from django.urls import path
from .views import *

urlpatterns = [
    path('employees/list/', EmployeeOnlyListView.as_view(), name='employee_only_list'),
    path('employees/', EmployeeListView.as_view(), name='employee_details_add_list'),
    path('employees/<pk>', EmployeeView.as_view(), name='employee_details_get_update_delete'),
    path('address/', AddressListView.as_view(), name='address_add_list'),
    path('address/<pk>', AddressView.as_view(), name='address_get_update_delete'),
]
