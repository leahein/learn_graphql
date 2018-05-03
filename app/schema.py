import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(
        name=graphene.String(default_value='stranger'))

    def resolve_hello(self, info, name):
        return f'Hello {name}'

SCHEMA = graphene.Schema(query=Query)

result = SCHEMA.execute('{hello {name}}')
print(result.data)
