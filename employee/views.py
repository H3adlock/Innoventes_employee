from .models import *
from .serializers import EmployeeSerializer, EmployeeOnlySerializer, AddressByEmployeeSerializer
from rest_framework import generics
from .permissions import IsAdminOrReadOnly


class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class EmployeeView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = (IsAdminOrReadOnly,)


class AddressListView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressByEmployeeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class AddressView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressByEmployeeSerializer
    queryset = Address.objects.all()
    permission_classes = (IsAdminOrReadOnly,)


class EmployeeOnlyListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeOnlySerializer
