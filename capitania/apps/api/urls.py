from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

app_name = 'api'
urlpatterns = [
    url('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True)))
]
