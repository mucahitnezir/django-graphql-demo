import graphene
import graphql_jwt

from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from user.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = 'password',


class Query(graphene.ObjectType):
    me = graphene.Field(UserType, token=graphene.String(required=True))

    @login_required
    def resolve_me(self, info, **kwargs):
        return info.context.user


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
