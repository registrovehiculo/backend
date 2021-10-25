import graphene
from graphene_django.types import ObjectType
from capitania.apps.api.types.provincias import *
from capitania.apps.api.types.vehiculo import VehiculoType
from capitania.apps.api.types.users import UserType
from capitania.apps.api.types.reviews import ReviewType, ReviewerAnswersType
from capitania.apps.api.types.shipment import ShipmentType
from capitania.apps.api.types.infogestiShipement import InfogestiShipmentType, ClienteType
from capitania.apps.api.queries.deleteRecords import deleteRecords
from capitania.apps.api.queries.PinarDelRio import ContributorsFromPinarQuery
from capitania.apps.api.queries.Artemisa import ContributorsFromArtemisaQuery
from capitania.apps.api.queries.Camaguey import ContributorsFromCamagueyQuery
from capitania.apps.api.queries.CiegoDeAvila import ContributorsFromCiegoDeAvilaQuery
from capitania.apps.api.queries.SanticEspiritud import ContributorsFromSanticEspiritudQuery
from capitania.apps.api.queries.Guantanamo import ContributorsFromGuantanamoQuery
from capitania.apps.api.queries.Holguin import ContributorsFromHolguinQuery
from capitania.apps.api.queries.Granma import ContributorsFromGranmaQuery
from capitania.apps.api.queries.IslaDeLaJuventud import ContributorsFromIslaDeLaJuventudQuery
from capitania.apps.api.queries.Matanzas import ContributorsFromMatanzasQuery
from capitania.apps.api.queries.Mayabeque import ContributorsFromMayabequeQuery
from capitania.apps.api.queries.Cienfuegos import ContributorsFromCienfuegosQuery
from capitania.apps.api.queries.SantiagoDeCuba import ContributorsFromSantiagoDeCubaQuery
from capitania.apps.api.queries.LasTunas import ContributorsFromLasTunasQuery
from capitania.apps.api.queries.VillaClara import ContributorsFromVillaClaraQuery
from capitania.apps.api.queries.LaHabana import ContributorsFromLaHabanaQuery
from capitania.apps.api.queries.RepeatedPlates import RepeatedPlatesQuery
from capitania.apps.api.queries.InfogestiContributors import ContributorsFromInfogestiQuery
from capitania.apps.api.queries.users import UserQuery
from capitania.apps.api.queries.shipment import ShipmentQuery
from capitania.apps.api.queries.Reviews import UserReviewsQuery, AllReviewsQuery, AllReviewsAnswersQuery, UserReviewAnswerQuery
from capitania.apps.api.queries.Vehiculo import VehiculoQuery
from capitania.apps.api.mutations import searches as searches_mutations
from capitania.apps.api.mutations import auth as auth_mutations
from capitania.apps.api.mutations import reviews as reviews_mutations
from capitania.apps.api.mutations import shipment as update_database
from capitania.apps.api.mutations import UpdateTransporte, UpdateEmbarcacion
from capitania.apps.api.mutations import auth, getUser, UpdateName


class Mutation(
    ObjectType
):
    login = auth_mutations.LoginMutation.Field()
    search = searches_mutations.SearchMutation.Field()
    update_review = reviews_mutations.UpdateReviewMutation.Field()
    remove_review = reviews_mutations.RemoveReviewMutation.Field()
    create_review = reviews_mutations.CreateReview.Field()
    create_review_answer = reviews_mutations.CreateReviewAnswer.Field()
    update_shipment_database = update_database.UpdateShipmentDatabase.Field()
    update_transporte = UpdateTransporte.UpdateTransporteDatabase.Field()
    update_embarcacion = UpdateEmbarcacion.UpdateEmbarcacionDatabase.Field()
    signup = auth.SignupMutation.Field()
    get_user = getUser.getUser.Field()
    delete_all_user = getUser.deleteAllUser.Field()
    update_name = UpdateName.UpdateName.Field()


class Query(
    ShipmentQuery,
    ContributorsFromVillaClaraQuery,
    ContributorsFromLasTunasQuery,
    ContributorsFromSantiagoDeCubaQuery,
    ContributorsFromCienfuegosQuery,
    ContributorsFromMayabequeQuery,
    ContributorsFromMatanzasQuery,
    ContributorsFromIslaDeLaJuventudQuery,
    ContributorsFromGranmaQuery,
    ContributorsFromHolguinQuery,
    ContributorsFromGuantanamoQuery,
    ContributorsFromSanticEspiritudQuery,
    ContributorsFromCiegoDeAvilaQuery,
    ContributorsFromCamagueyQuery,
    ContributorsFromArtemisaQuery,
    ContributorsFromPinarQuery,
    ContributorsFromInfogestiQuery,
    ContributorsFromLaHabanaQuery,
    deleteRecords,
    UserQuery,
    VehiculoQuery,
    UserReviewsQuery,
    AllReviewsQuery,
    AllReviewsAnswersQuery,
    UserReviewAnswerQuery,
    RepeatedPlatesQuery,
    ObjectType,
):
    pass


types = [
    UserType,
    ArtemisaType,
    PinarDelRioType,
    CamagueyType,
    CiegoDeAvilaType,
    CienfuegosType,
    GranmaType,
    GuantanamoType,
    HolguinType,
    IslaDeLaJuventudType,
    LasTunasType,
    MayabequeType,
    SantiagoDeCubaType,
    SanticEspiritudType,
    VillaClaraType,
    MatanzasType,
    LaHabanaType,
    VehiculoType,
    InfogestiContributorsType,
    UserType,
    InfogestiShipmentType,
    ShipmentType,
    ClienteType,
    ReviewType,
    ReviewerAnswersType
]
schema = graphene.Schema(query=Query, mutation=Mutation, types=types)
