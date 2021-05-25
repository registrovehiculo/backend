import graphene

from capitania.apps.api.types.reviews import ReviewType
from capitania.apps.core.models import User, Review


class UserReviewsQuery:
    user_reviews = graphene.List(ReviewType, username=graphene.String())

    def resolve_user_reviews(self, info, username=graphene.String()):
        user = User.objects.get(username__iexact=username, is_active=True)
        return Review.objects.filter(reviewer=user)


class AllReviewsQuery:
    all_reviews = graphene.List(ReviewType)

    def resolve_all_reviews(self, info):
        return Review.objects.all()