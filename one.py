import graphene
import json


class Query(graphene.ObjectType):
    name = graphene.String()

    def resolve_name(self, info):
        return 'Hello User'


schema = graphene.Schema(query=Query)
result = schema.execute("""
    query{
        name
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


