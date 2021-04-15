from graphene_django.types import DjangoObjectType
from capitania.apps.core.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        only_fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'genre',
            'email',
            'date_joined',
            'is_active',
            'first_login',
            'is_superuser'
        )

