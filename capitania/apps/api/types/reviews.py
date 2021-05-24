from graphene_django.types import DjangoObjectType
from capitania.apps.core.models import Review


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
