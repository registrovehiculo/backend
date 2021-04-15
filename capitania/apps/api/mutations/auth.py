import graphene
from graphql import GraphQLError
from django.utils.timezone import now
from django.contrib.auth.hashers import check_password
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from capitania.apps.api.types.users import UserType
from capitania.apps.core.models import User


class LoginMutation(graphene.Mutation):
    status = graphene.String()
    token = graphene.String()
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        try:
            user = User.objects.get(username__iexact=username, is_active=True)

            if user and check_password(password=password, encoded=user.password):
                # Time is recorded
                login_datetime = now()
                user.last_login = login_datetime

                # Response without first_login
                payload = jwt_payload_handler(user)
                response = LoginMutation(status='ok', token=jwt_encode_handler(payload), user=user)

                # First login is recorded
                if user.first_login is None:
                    user.first_login = login_datetime
                user.save()
                return response
            else:
                return LoginMutation(status='error')
        except User.DoesNotExist:
            pass
            return LoginMutation(status='error')
        except:
            raise GraphQLError(message='error')
