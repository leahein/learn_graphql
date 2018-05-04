import graphene

class Query(graphene.ObjectType):
    person = graphene.String(
        name=graphene.String(default_value='stranger')
    )

    def resolve_person(self, info, name):
        return f'Hello {name}'

class PersonMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    ok = graphene.Boolean(required=True)

    def mutate(self, info, name):
        if name:
            return PersonMutation(ok=True)
        return PersonMutation(ok=False)

class Mutation(graphene.ObjectType):
    person = PersonMutation.Field()

SCHEMA = graphene.Schema(query=Query, mutation=Mutation)
