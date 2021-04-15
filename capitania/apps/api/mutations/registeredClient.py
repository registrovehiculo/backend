import graphene
from graphql import GraphQLError

from capitania.apps.api.types.infogestiShipement import ClienteType, InfogestiShipmentType
from capitania.apps.core.models import Cliente, InfogestiShipment


class RegisteredClient(graphene.Mutation):
    client = graphene.List(ClienteType)
    status = graphene.String()

    class Arguments:
        arr = graphene.List(graphene.String)

    def mutate(self, info, arr):
        client = Cliente.objects.raw(
        'Select * from CLIENTE_EMBARCACION@infogesti ce inner join CLIENTE@infogesti ci on ci.id = ce.id_cliente inner join CORE_SHIPMENT t on t.OWNER_NAME = ci.NOMBRE_COMPLETO')
        # print('*****************************************')
        client = Cliente.objects.all()
        # asd = InfogestiShipment.objects.all()
        # print(asd)
        # client = Cliente.objects.filter(id=0)
        # 'Select * from CLIENTE@infogesti ci inner join CLIENTE_EMBARCACION@infogesti ce on ci.id = ce.id_cliente')
        # clientList = list(client)
        # print(clientList)
        return RegisteredClient(
            status='ok',
            client=client
        )
    # except:
    # raise GraphQLError(message='error')
