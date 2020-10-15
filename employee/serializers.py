from rest_framework import serializers
from .models import Employee, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'address_type',
                  'address_line_1',
                  'address_line_2',
                  'city',
                  'pin',
                  'country')


class EmployeeSerializer(serializers.ModelSerializer):
    address_employee = AddressSerializer(source='address_set', many=True)

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'designation', 'address_employee')

    def create(self, validated_data):
        addresses_data = validated_data.pop('address_employee')
        employee = Employee.objects.create(**validated_data)
        for addresses_data in addresses_data:
            Address.objects.create(employee=employee, **addresses_data)
        return employee

    def update(self, instance, validated_data):
        addresses_data = validated_data.pop('address_employee')
        addresses = (instance.address_employee).all()
        addresses = list(addresses)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.save()

        for single_address in addresses_data:
            address = addresses.pop(0)
            address.address_type = single_address.get('address_type', address.address_type)
            address.address_line_1 = single_address.get('address_line_1', address.address_line_1)
            address.address_line_2 = single_address.get('address_line_2', address.address_line_2)
            address.city = single_address.get('city', address.city)
            address.pin = single_address.get('pin', address.pin)
            address.country = single_address.get('release_date', address.country)
            address.save()
        return instance


class EmployeeOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'designation')


class AddressByEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id','employee', 'address_type',
                  'address_line_1',
                  'address_line_2',
                  'city',
                  'pin',
                  'country')