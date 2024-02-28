import graphene


class Query(graphene.ObjectType):
    name = graphene.String(username=graphene.String(default_value="World"))

    def resolve_name(self, info, username):
        return f"Hello {info.context.get('user')}"


schema = graphene.Schema(query=Query)
result = schema.execute("""
    query{
        name
    }
""", context={"user": "alex"})

print(result.data)
