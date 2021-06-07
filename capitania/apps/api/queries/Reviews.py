import graphene

from capitania.apps.api.types.reviews import ReviewType, ReviewerAnswersType
from capitania.apps.core.models import User, Review, ReviewerAnswers


class UserReviewsQuery:
    user_reviews = graphene.List(ReviewType, username=graphene.String())

    def resolve_user_reviews(self, info, username=graphene.String()):
        user = User.objects.get(username__iexact=username, is_active=True)
        return Review.objects.filter(reviewer=user)


class AllReviewsQuery:
    all_reviews = graphene.List(ReviewType)

    def resolve_all_reviews(self, info):
        return Review.objects.all().order_by('-created_at')


class AllReviewsAnswersQuery:
    all_reviews_answers = graphene.List(ReviewerAnswersType)

    def resolve_all_reviews_answers(self, info):
        return ReviewerAnswers.objects.all()


class UserReviewAnswerQuery:
    user_review_answer = graphene.List(ReviewerAnswersType, review_id=graphene.Int())

    def resolve_user_review_answer(self, info, review_id):
        return ReviewerAnswers.objects.filter(reviewer_answers_id=review_id)