import graphene
from graphql import GraphQLError
from capitania.apps.api.types.vehiculo import VehiculoType
from capitania.apps.core.models import Vehiculo
from django.db.models import Q


class SearchMutation(graphene.Mutation):
    vehiculo = graphene.List(VehiculoType)
    status = graphene.String()

    class Arguments:
        criteria = graphene.String(required=True)

    def mutate(self, info, criteria):
        try:
            vehiculo = Vehiculo.objects.exclude(Q(datospersona__isnull=True) | Q(datospersona='')).filter(
                datospersona__istartswith=criteria).distinct()[:20]
            return SearchMutation(
                status='ok',
                vehiculo=vehiculo
            )
        except:
            raise GraphQLError(message='error')