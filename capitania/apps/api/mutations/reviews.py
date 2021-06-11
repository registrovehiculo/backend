import graphene
from graphql import GraphQLError
from django.utils.timezone import now

from capitania.apps.api.types.reviews import ReviewType, ReviewerAnswersType
from capitania.apps.core.models import Review, User, ReviewerAnswers


class UpdateReviewMutation(graphene.Mutation):
    status = graphene.String()
    review = graphene.Field(ReviewType)

    class Arguments:
        id = graphene.Int(required=True)
        text = graphene.String(required=True)

    def mutate(self, info, id, text):
        try:
            review = Review.objects.get(pk=id)
            review.save()
        except review.DoesNotExist:
            pass
            review.text = text
            review.updated_at = now()
            review.save()
            return UpdateReviewMutation(status='ok', review=review)
        except:
            raise GraphQLError(message='error')


class RemoveReviewMutation(graphene.Mutation):
    status = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        try:
            review = Review.objects.get(pk=id)
        except review.DoesNotExist:
            pass
        review.delete()
        return UpdateReviewMutation(status='ok')


class CreateReview(graphene.Mutation):
    status = graphene.String()
    review = graphene.Field(ReviewType)

    class Arguments:
        text = graphene.String(required=True)
        username = graphene.String(required=True)

    def mutate(self, info, username, text):
        user = User.objects.get(username__iexact=username, is_active=True)
        review = Review.objects.create(text=text, reviewer=user)
        print(review)
        review.save()
        return CreateReview(status='ok', review=review)


class CreateReviewAnswer(graphene.Mutation):
    status = graphene.String()
    reviewer_answers = graphene.Field(ReviewerAnswersType)

    class Arguments:
        text = graphene.String(required=True)
        review_id = graphene.Int(required=True)
        username = graphene.String(required=True)

    def mutate(self, info, review_id, text, username):
        review = Review.objects.get(pk=review_id)
        reviewer_answers = ReviewerAnswers.objects.create(text=text, reviewer_answers=review, username=username)
        reviewer_answers.save()
        return CreateReviewAnswer(status='ok', reviewer_answers=reviewer_answers)


