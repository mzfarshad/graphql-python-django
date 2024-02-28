import graphene
import uuid
from datetime import datetime
import json


class User(graphene.ObjectType):
    id = graphene.ID(default_value=uuid.uuid4())
    username = graphene.String()
    created_at = graphene.DateTime(default_value=datetime.now())
    email = graphene.String()


class UserInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    email = graphene.String(required=True)


class CreateUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        user_data = UserInput(required=True)

    def mutate(self, info, user_data):
        user = User(username=user_data.username, email=user_data.email )
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=User, mutation=Mutation)

result = schema.execute("""
    mutation {
        createUser(userData:{
            username:"kevin",
            email:"kevin@email.com"
        }) {
            user {
                id
                username
                email
                createdAt
            }
        }
    }
""")

print(result.data)

j = json.dumps(dict(result.data), indent=2)

print(j)
