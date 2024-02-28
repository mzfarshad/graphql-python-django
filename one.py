import graphene
import json


class Query(graphene.ObjectType):
    name = graphene.String(username=graphene.String(default_value='farshad'))

    def resolve_name(self, info, username):
        return f'Hello {username}'


schema = graphene.Schema(query=Query)
result = schema.execute("""
    query{
        name(username:"mahour")
    }
""")

print(result)
print('===>> result is a dictionary <<===')
print(result.data)
print(result.data.values())
print(result.data.keys())
print(result.data['name'])

j = json.dumps(dict(result.data), indent=2)
print(j)


