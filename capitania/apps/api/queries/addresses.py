import graphene
from capitania.apps.api.types.adresses import CityType, CountryType, StateType
from capitania.apps.core.models import Country, State, City


class AddressQuery:
    countries = graphene.List(CountryType)
    states = graphene.List(StateType, country_id=graphene.String())
    cities = graphene.List(CityType, state_id=graphene.Int())
    cities_by_id = graphene.Field(CityType, city_id=graphene.Int())

    def resolve_countries(self, info):
        return Country.objects.all()

    def resolve_states(self, info, country_id=graphene.String()):
        return State.objects.filter(country_id=country_id)

    def resolve_cities(self, info, state_id=graphene.Int()):
        return City.objects.filter(state=state_id)

    def resolve_cities_by_id(self, info, city_id=graphene.Int()):
        return City.objects.get(id=city_id)

