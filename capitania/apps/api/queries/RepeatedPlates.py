import graphene
from capitania.apps.api.types.infogestiShipement import ClienteType
from capitania.apps.core.models import Matanzas, Cliente


class RepeatedPlatesQuery(graphene.ObjectType):
    repeated = graphene.List(ClienteType)

    def resolve_repeated(self, info):
        return Cliente.objects.raw('select c.id, C.DPA, C.NIT, c.nombre_completo, TT.MATRICULA from CLIENTE@INFOGESTI C INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID and C.tipo_persona=1 WHERE (c.nit, tt.matricula) '
                                   'in (select distinct c.nit, tt.matricula from  CLIENTE@INFOGESTI C INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID  and C.tipo_persona=1 GROUP BY c.nit, tt.matricula HAVING COUNT(*) > 1) order by c.nit')
