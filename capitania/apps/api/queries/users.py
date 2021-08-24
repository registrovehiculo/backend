import graphene

from django.contrib.auth import get_user_model

from capitania.apps.api.types.users import UserType
from capitania.apps.core.models import User


class UserQuery:
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_check_email(self, info, email=None):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            pass
        return None