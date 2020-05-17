import graphene
import book.schema

class Query(book.schema.Query ,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)