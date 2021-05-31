from graphene_django.types import DjangoObjectType
from capitania.apps.core.models import Review, ReviewerAnswers


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review


class ReviewerAnswersType(DjangoObjectType):
    class Meta:
        model = ReviewerAnswers
