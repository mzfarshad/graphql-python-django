import graphene


class Query(graphene.ObjectType):
    name = graphene.String(username=graphene.String(default_value="World"))

    def resolve_name(self, info, username):
        return f"Hello {username}"


schema = graphene.Schema(query=Query)
result = schema.execute("""
    query{
        name(username:"jan")
    }
""")

print(result.data)
