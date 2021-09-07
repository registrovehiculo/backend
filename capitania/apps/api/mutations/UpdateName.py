import graphene
from graphql import GraphQLError

from capitania.apps.core.models import Artemisa, LaHabana, LasTunas, IslaDeLaJuventud, Camaguey, CiegoDeAvila, \
    Cienfuegos, Guantanamo, Holguin, Matanzas, PinarDelRio, SanticEspiritud, SantiagoDeCuba, VillaClara, Granma, \
    Mayabeque


class UpdateName(graphene.Mutation):
    status = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)
        province = graphene.String(required=True)
        info_gesti_name = graphene.String(required=True)

    def mutate(self, info, id, province, info_gesti_name):
        print(province + ' asdfsd')
        try:
            print(province + ' ' + 'adfawds')
            if province == 'artemisa':
                artemisa = Artemisa.objects.get(pk=id)
                if artemisa is not None:
                    artemisa.datospersona = info_gesti_name

            if province == 'habana':
                habana = LaHabana.objects.get(pk=id)
                if habana is not None:
                    LaHabana.datospersona = info_gesti_name

            if province == 'lasTunas':
                lasTunas = LasTunas.objects.get(pk=id)
                if lasTunas is not None:
                    lasTunas.datospersona = info_gesti_name
                    return UpdateName(status='ok')

            if province == 'islaDeLaJuventud':
                islaDeLaJuventud = IslaDeLaJuventud.objects.get(pk=id)
                if islaDeLaJuventud is not None:
                    islaDeLaJuventud.datospersona = info_gesti_name
                    return UpdateName(status='ok')

            if province == 'camaguey':
                camaguey = Camaguey.objects.get(pk=id)
                print(camaguey)
                print('asdf')

                if camaguey is not None:
                    print('whaaat')
                    camaguey.datospersona = info_gesti_name
                    print(camaguey.datospersona)
                    return UpdateName(status='ok')

            if province == 'ciegoDeAvila':
                ciegoDeAvila = CiegoDeAvila.objects.get(pk=id)
                if ciegoDeAvila is not None:
                    ciegoDeAvila.datospersona = info_gesti_name
                    return UpdateName(status='ok')

            if province == 'cienfuegos':
                cienfuegos = Cienfuegos.objects.get(pk=id)
                if cienfuegos is not None:
                    print(cienfuegos.datospersona)
                    cienfuegos.datospersona = info_gesti_name
                    return UpdateName(status='ok')

            if province == 'guantanamo':
                guantanamo = Guantanamo.objects.get(pk=id)
                if guantanamo is not None:
                    guantanamo.datospersona = info_gesti_name
                    return UpdateName(status='ok')

            if province == 'holguin':
                holguin = Holguin.objects.get(pk=id)
                if holguin is not None:
                    holguin.datospersona = info_gesti_name
                    return UpdateName(status='ok')

            if province == 'matanzas':
                matanzas = Matanzas.objects.get(pk=id)
                if matanzas is not None:
                    matanzas.datospersona = info_gesti_name
                    return UpdateName(status='ok')

            if province == 'pinarDelRio':
                pinarDelRio = PinarDelRio.objects.get(pk=id)
                if pinarDelRio is not None:
                    pinarDelRio.datospersona = info_gesti_name
                    return UpdateName(status='ok')

            if province == 'santciSpiritus':
                santciSpiritus = SanticEspiritud.objects.get(pk=id)
                if santciSpiritus is not None:
                    santciSpiritus.datospersona = info_gesti_name
                    return UpdateName(status='ok')

            if province == 'santiagoDeCuba':
                santiagoDeCuba = SantiagoDeCuba.objects.get(pk=id)
                if santiagoDeCuba is not None:
                    santiagoDeCuba.datospersona = info_gesti_name
                    return UpdateName(status='ok')

            if province == 'villaClara':
                villaClara = VillaClara.objects.get(pk=id)
                if villaClara is not None:
                    villaClara.datospersona = info_gesti_name
                    return UpdateName(status='ok')

            if province == 'granma':
                granma = Granma.objects.get(pk=id)
                if granma is not None:
                    granma.datospersona = info_gesti_name
                    return UpdateName(status='ok')

            if province == 'mayabeque':
                mayabeque = Mayabeque.objects.get(pk=id)
                if mayabeque is not None:
                    mayabeque.datospersona = info_gesti_name
                    return UpdateName(status='ok')


        except:
            raise GraphQLError(message='error')
