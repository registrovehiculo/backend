import graphene
from django.db import connections
from rest_framework.utils import json

from capitania.apps.api.types.shipment import ShipmentType
from capitania.apps.core.models import Shipment


class UpdateShipmentDatabase(graphene.Mutation):
    status = graphene.String()

    class Arguments:
        data = graphene.JSONString(required=True)

    def mutate(self, info, data):
        cursor = connections['default'].cursor()
        Shipment.objects.all().delete()
        id_number = ''
        province_number = ''
        owner_name = ''
        registry_number = ''
        shipment_name = ''
        captaincy_province = ''
        base_name = ''
        for arr in data:
            if 'Carné identidad' in arr.keys():
                id_number = arr['Carné identidad']
            if 'Prov' in arr.keys():
                province_number = arr['Prov']
            if 'Propietarios' in arr.keys():
                owner_name = arr['Propietarios']
            if 'Número de registro' in arr.keys():
                registry_number = arr['Número de registro'],
            if 'Embarcación' in arr.keys():
                shipment_name = arr['Embarcación'],
            if 'Capitanía' in arr.keys():
                captaincy_province = arr['Capitanía'],
            if 'Basificación' in arr.keys():
                base_name = arr['Basificación']
            cursor.execute(
             "INSERT INTO CORE_SHIPMENT (PROVINCE_NUMBER, ID_NUMBER, OWNER_NAME, REGISTRY_NUMBER, SHIPMENT_NAME, CAPTAINCY_PROVINCE, BASE_NAME) VALUES (%s, %s, %s, %s, %s, %s, %s)",
             [province_number, id_number, owner_name, registry_number[0], shipment_name[0], captaincy_province[0], base_name])
        return UpdateShipmentDatabase(status='ok')
#         book = xlrd.open_workbook("/home/edward/Desktop/base de datos capitania/BD Capitania.xls")
#         print("The number of worksheets is {0}".format(book.nsheets))
#         print("Worksheet name(s): {0}".format(book.sheet_names()))
#         sheet = book.sheet_by_index(0)
#
#         for r in range(1, sheet.nrows):
#             province_number = sheet.cell(r, 0).value
#             id_number = sheet.cell(r, 1).value
#             owner_name = sheet.cell(r, 2).value
#             registry_number = sheet.cell(r, 3).value
#             shipment_name = sheet.cell(r, 4).value
#             captaincy_province = sheet.cell(r, 5).value
#             base_name = sheet.cell(r, 6).value
#             cursor = connections['default'].cursor()
#             cursor.execute(
#                 "INSERT INTO CORE_SHIPMENT (PROVINCE_NUMBER, ID_NUMBER, OWNER_NAME, REGISTRY_NUMBER, SHIPMENT_NAME, CAPTAINCY_PROVINCE, BASE_NAME) VALUES (%s, %s, %s, %s, %s, %s, %s)",
#                 [province_number, id_number, owner_name, registry_number, shipment_name, captaincy_province, base_name])