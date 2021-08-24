import graphene
from django.db import connections
import xlrd
from graphql import GraphQLError

from capitania.apps.core.models import PinarDelRio, Artemisa, Camaguey, CiegoDeAvila, Cienfuegos, Granma, Guantanamo, \
    Holguin, IslaDeLaJuventud, LasTunas, Matanzas, Mayabeque, SantiagoDeCuba, SanticEspiritud, VillaClara, LaHabana


class UpdateTransporteDatabase(graphene.Mutation):
    status = graphene.String()

    def mutate(self, info):
        try:
            book = xlrd.open_workbook("/home/edward/Transporte/PINAR DEL RIO.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            PinarDelRio.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_PINARDELRIO ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])

            book = xlrd.open_workbook("/home/edward/Transporte/ARTEMISA.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            Artemisa.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_ARTEMISA ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])

            book = xlrd.open_workbook("/home/edward/Transporte/CAMAGUEY.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            Camaguey.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_CAMAGUEY ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])

            book = xlrd.open_workbook("/home/edward/Transporte/CIEGO DE AVILA.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            CiegoDeAvila.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_CIEGODEAVILA ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])

            book = xlrd.open_workbook("/home/edward/Transporte/CIENFUEGOS.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            Cienfuegos.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_CIENFUEGOS ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])

            book = xlrd.open_workbook("/home/edward/Transporte/GRANMA.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            Granma.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_GRANMA ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])

            book = xlrd.open_workbook("/home/edward/Transporte/GUANTANAMO.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            Guantanamo.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_GUANTANAMO ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])
            book = xlrd.open_workbook("/home/edward/Transporte/HOLGUIN.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            Holguin.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_HOLGUIN ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])
            book = xlrd.open_workbook("/home/edward/Transporte/ISLA.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            IslaDeLaJuventud.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_ISLADELAJUVENTUD ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])
            book = xlrd.open_workbook("/home/edward/Transporte/LAS TUNAS.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            LasTunas.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_LASTUNAS ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])
            book = xlrd.open_workbook("/home/edward/Transporte/MATANZAS.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            Matanzas.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_MATANZAS ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])

            book = xlrd.open_workbook("/home/edward/Transporte/MAYABEQUE.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            Mayabeque.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_MAYABEQUE ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])
            book = xlrd.open_workbook("/home/edward/Transporte/SANTIAGO DE CUBA.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            SantiagoDeCuba.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_SANTIAGODECUBA ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])

            book = xlrd.open_workbook("/home/edward/Transporte/S SPIRITUS.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            SanticEspiritud.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_SANTICESPIRITUD ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])

            book = xlrd.open_workbook("/home/edward/Transporte/VILLA CLARA.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            VillaClara.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_VILLACLARA ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])
            book = xlrd.open_workbook("/home/edward/Transporte/HABANA1.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            LaHabana.objects.all().delete()
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_LAHABANA ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])

            book = xlrd.open_workbook("/home/edward/Transporte/HABANA2.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_LAHABANA ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])

            book = xlrd.open_workbook("/home/edward/Transporte/HABANA3.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_LAHABANA ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])
            book = xlrd.open_workbook("/home/edward/Transporte/HABANA4.xls")
            print("The number of worksheets is {0}".format(book.nsheets))
            print("Worksheet name(s): {0}".format(book.sheet_names()))
            sheet = book.sheet_by_index(0)
            for r in range(1, sheet.nrows):
                municipio = sheet.cell(r, 0).value
                estado_vehiculo = sheet.cell(r, 1).value
                marca_vehiculo = sheet.cell(r, 2).value
                chapa_nueva = sheet.cell(r, 3).value
                numero_motor = sheet.cell(r, 4).value
                numero_carroseria = sheet.cell(r, 5).value
                marca_motor = sheet.cell(r, 6).value
                numero_identidad = sheet.cell(r, 7).value
                datos_persona = sheet.cell(r, 8).value
                direccion = sheet.cell(r, 9).value
                cursor = connections['default'].cursor()
                cursor.execute(
                    "Insert into CORE_LAHABANA ( MUNICIPIO, ESTADOVEHICULO, MARCAVEHICULO, CHAPANUEVA, NUMEROMOTOR, "
                    "NUMEROCARROSERIA, MARCAMOTOR, NUMEROIDENTIDAD, DATOSPERSONA, DIRECCION)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [municipio, estado_vehiculo, marca_vehiculo, chapa_nueva, numero_motor,
                     numero_carroseria, marca_motor, numero_identidad, datos_persona, direccion])
            return UpdateTransporteDatabase(status='ok')
        except:
            raise GraphQLError(message='error')
