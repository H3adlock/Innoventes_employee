from django.urls import path
from .views import *

urlpatterns = [
    # path('movies', MovieListView.as_view(), name='api'),
    # path('movies/create', MovieCreateView.as_view(), name='api_create'),
    # path('movies/details/<pk>', MovieDetailView.as_view(), name='api_update_delete')
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/add', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<pk>', EmployeeEditView.as_view(), name='employee_update_delete'),
    path('employees/details/<pk>', EmployeeDetailsView.as_view(), name='employee_details_list')
]
