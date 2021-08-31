import graphene
from django.db import connections
from graphql import GraphQLError
import xlrd
from capitania.apps.core.models import Shipment


class UpdateEmbarcacionDatabase(graphene.Mutation):
    status = graphene.String()

    def mutate(self, info):
        try:
            book = xlrd.open_workbook(r'C:\Embarcaciones\Embarcacion.xls')
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            Shipment.objects.all().delete()
            for r in range(1, sheet.nrows):
                province_number = sheet.cell(r, 0).value
                id_number = sheet.cell(r, 1).value
                owner_name = sheet.cell(r, 2).value
                registry_number = sheet.cell(r, 3).value
                shipment_name = sheet.cell(r, 4).value
                captaincy_province = sheet.cell(r, 5).value
                base_name = sheet.cell(r, 6).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_SHIPMENT (PROVINCE_NUMBER, ID_NUMBER, OWNER_NAME, REGISTRY_NUMBER, "
                    "SHIPMENT_NAME, CAPTAINCY_PROVINCE, BASE_NAME) "
                    "values (%s, %s, %s, %s, %s, %s, %s)",
                    [province_number, id_number, owner_name, registry_number, shipment_name, captaincy_province,
                     base_name])
            return UpdateEmbarcacionDatabase(status='ok')
        except:
            raise GraphQLError(message='error')
