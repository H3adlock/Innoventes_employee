from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Employee, Address
from .serializers import EmployeeOnlySerializer, AddressByEmployeeSerializer
from django.urls import reverse


class EmployeeAddTest(APITestCase):
    client = APIClient()

    @staticmethod
    def add_employee(first_name="", last_name="", birth_date="", designation=""):
        if first_name != "" and designation != "":
            Employee.objects.create(first_name=first_name, last_name=last_name, birth_date=birth_date,
                                    designation=designation)

    def setUp(self):
        self.add_employee("Santanu", "Bose", "1994-07-14", "Software Engineer")
        self.add_employee("Nitish", "Singh", "1993-08-17", "Senior Software Engineer")
        self.add_employee("Subhajit", "Pal", "1994-08-07", "Software Engineer")
        self.add_employee("Sourav", "Ghosh", "1994-08-05", "Software Engineer")


class ListEmployeesTest(EmployeeAddTest):
    def test_list_employees(self):
        response = self.client.get(
            reverse("employee_only_list")
        )
        expected = Employee.objects.all()
        serialized = EmployeeOnlySerializer(expected, many=True)
        print(response.data)
        print(serialized.data)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AddressAddTest(APITestCase):
    client = APIClient()
    @staticmethod
    def add_address(employee_id="", address_type="", address_line_1="", address_line_2="", city="", pin="", country=""):
        if employee_id != "" and address_type != "" and address_line_1 != "" and city != "":
            employee = Employee.objects.get(pk=employee_id)
            Address.objects.create(employee=employee, address_type=address_type, address_line_1=address_line_1,
                                   address_line_2=address_line_2,
                                   pin=pin, country=country)

    def setUp(self):
        self.add_address(1, "Office address", "Sector V", "WestBengal", "Kolkata", 15484, "India")
        self.add_address(2, "Office address", "Sector V", "WestBengal", "Kolkata", 15484, "India")
        self.add_address(3, "Office address", "Sector V", "WestBengal", "Kolkata", 15484, "India")
        self.add_address(4, "Office address", "Sector V", "WestBengal", "Kolkata", 15484, "India")


class ListAddressTest(AddressAddTest):
    def test_list_address(self):
        response = self.client.get(
            reverse("address_add_list")
        )
        expected = Address.objects.all()
        serialized = AddressByEmployeeSerializer(expected, many=True)
        print(response.data)
        print(serialized.data)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
