import graphene
from django.db import connections
from capitania.apps.core.models import PinarDelRio


class UpdatePinarDelRioDatabase(graphene.Mutation):
    status = graphene.String()

    class Arguments:
        data = graphene.JSONString(required=True)

    def mutate(self, info, data):
        print('1')
        cursor = connections['default'].cursor()
        print('2')
        PinarDelRio.objects.all().delete()
        municipio = ''
        estado_vehiculo = ''
        marca_vehiculo = ''
        chapa_nueva = ''
        numero_motor = ''
        numero_carroseria = ''
        marca_motor=''
        numero_identidad=''
        datos_persona=''
        direccion=''
        for arr in data:
            print(arr['Nro de Identidad'])
            if 'Municipio Residencia Largo' in arr.keys():
                municipio = arr['Municipio Residencia Largo']
            if 'Estado del Vehículo' in arr.keys():
                estado_vehiculo = arr['Estado del Vehículo']
            if 'Marca del Vehículo' in arr.keys():
                marca_vehiculo = arr['Marca del Vehículo']
            if 'Chapa Nueva' in arr.keys():
                chapa_nueva = arr['Chapa Nueva'],
            if 'Nro de Motor' in arr.keys():
                numero_motor = arr['Nro de Motor'],
            if 'Nro de Carroseria' in arr.keys():
                numero_carroseria = arr['Nro de Carroseria'],
            if 'Marca del Motor' in arr.keys():
                marca_motor = arr['Marca del Motor']
            if 'Nro de Identidad' in arr.keys():
                numero_identidad = arr['Nro de Identidad']
            if 'Generales de la Persona' in arr.keys():
                datos_persona = arr['Generales de la Persona']
            if 'Dirección' in arr.keys():
                direccion = arr['Dirección']
            cursor.execute(
             "INSERT INTO CORE_PINARDELRIO (MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
             "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION) VALUES "
             "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
             [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor, numero_carroseria, marca_motor,
              numero_identidad, datos_persona, direccion])
        return UpdatePinarDelRioDatabase(status='ok')
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