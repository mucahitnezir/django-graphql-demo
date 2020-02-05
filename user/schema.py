import graphene
from graphene_django import DjangoObjectType

from user.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = 'password',


class Query(graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(self, info, **kwargs):
        if not info.context.user.is_authenticated():
            return None
        return info.context.user
