import graphene
from django.views.generic import list

from capitania.apps.api.types.infogestiShipement import ClienteType
from capitania.apps.core.models import Cliente


class getClientFromId(graphene.Mutation):
    client = graphene.List(ClienteType)

    class Arguments:
        client_id = graphene.String(required=True)

    def mutate(self, info, client_id):
        # placeholders = ', '.join(['%s'] * len(client_id))
        print(client_id)
        cliente = Cliente.objects.raw("select * from cliente@infogesti c inner join cliente_tt@infogesti tt on c.id = tt.id_cliente WHERE c.nit LIKE %s", [client_id])
        # print('qwe')
        # cliente = Cliente.objects.filter(nit__in=client_id)
        return getClientFromId(client=cliente)