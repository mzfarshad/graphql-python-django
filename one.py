import graphene
import uuid
from datetime import datetime
import json


class User(graphene.ObjectType):
    id = graphene.ID(default_value=uuid.uuid4())
    username = graphene.String()
    created_at = graphene.DateTime(default_value=datetime.now())


class CreateUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        userName = graphene.String()

    def mutate(self, info, **kwargs):
        user = User(username=kwargs["userName"])
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=User, mutation=Mutation)

result = schema.execute("""
    mutation {
        createUser(userName:"jack") {
            user {
                id
                username
                createdAt
            }
        }
    }
""")

print(result.data)

j = json.dumps(dict(result.data), indent=2)

print(j)
