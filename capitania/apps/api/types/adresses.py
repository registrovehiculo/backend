from graphene_django.types import DjangoObjectType
from capitania.apps.core.models import Address, Country, State, City


class AddressType(DjangoObjectType):
    class Meta:
        model = Address


class CountryType(DjangoObjectType):
    class Meta:
        model = Country


class StateType(DjangoObjectType):
    class Meta:
        model = State


class CityType(DjangoObjectType):
    class Meta:
        model = City
