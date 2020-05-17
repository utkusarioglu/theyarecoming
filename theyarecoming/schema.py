import graphene
import theyarecoming.book.schema

class Query(graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)