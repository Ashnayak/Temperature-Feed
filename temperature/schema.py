import graphene

class Subscription(graphene.ObjectType):
    temperature = graphene.Float()

class Query(graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)
