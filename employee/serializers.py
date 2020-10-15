from rest_framework import serializers
from .models import Employee, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('address_type',
                  'address_line_1',
                  'address_line_2',
                  'city',
                  'pin',
                  'country')


class EmployeeWithAddressSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(source='address_set', many=True)

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'designation', 'addresses')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'designation')

