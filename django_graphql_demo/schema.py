import graphene

import book.schema
import user.schema


class Query(
    book.schema.Query,
    user.schema.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    book.schema.Mutation,
    user.schema.Mutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
