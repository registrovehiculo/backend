import graphene
from rest_framework.utils import json

from capitania.apps.api.types.shipment import ShipmentType
from capitania.apps.core.models import Shipment


class UpdateShipmentDatabase(graphene.Mutation):
    status = graphene.String()

    class Arguments:
        data = graphene.JSONString(required=True)

    def mutate(self, info, data):
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
            updated_data = Shipment.objects.create(
                province_number=province_number,
                id_number=id_number,
                owner_name=owner_name,
                registry_number=registry_number,
                shipment_name=shipment_name,
                captaincy_province=captaincy_province,
                base_name=base_name
                )
            updated_data.save()
        return UpdateShipmentDatabase(status='ok')
