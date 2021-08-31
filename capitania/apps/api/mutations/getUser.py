import graphene
from graphql import GraphQLError

from capitania.apps.api.types.users import UserType
from capitania.apps.core.models import User


class getUser(graphene.Mutation):
    user = graphene.Field(UserType)
    status = graphene.String()

    class Arguments:
        username = graphene.String(required=True)

    def mutate(self, info, username):
        try:
            user = User.objects.get(username=username)
            return getUser(status='error', user=user)
        except User.DoesNotExist:
            pass
            return getUser(status='ok')


class deleteAllUser(graphene.Mutation):
    user = graphene.Field(UserType)
    status = graphene.String()

    def mutate(self, info):
        user = User.objects.all().delete()
        return deleteAllUser(status='ok', user=user)
