from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee, Address
from .serializers import AddressSerializer, EmployeeSerializer, EmployeeWithAddressSerializer, \
    EmployeeOnlyWithAllAddressesSerializer
from .permissions import IsAdminOrReadOnly


class EmployeeCreateView(generics.CreateAPIView):
    """
        API view adding Employees
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class EmployeeEditView(generics.RetrieveUpdateDestroyAPIView):
    """
        API view update and delete
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class EmployeeListView(APIView):
    """
    API view for searching Employees
    """
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        queryset = Employee.objects.all()
        allowed_methods = ['GET']
        first_name = request.query_params.get('fname', None)
        if first_name is not None:
            queryset = queryset.filter(first_name__icontains=first_name)

        last_name = request.query_params.get('lname', None)
        if last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EmployeeDetailsView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeWithAddressSerializer


class EmployeeAddressEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeOnlyWithAllAddressesSerializer
    permission_classes = (IsAdminOrReadOnly,)


class EmployeeAddressCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeOnlyWithAllAddressesSerializer
    permission_classes = (IsAdminOrReadOnly,)