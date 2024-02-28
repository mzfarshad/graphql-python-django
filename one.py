import graphene
import uuid
from datetime import datetime
import json


class User(graphene.ObjectType):
    id = graphene.ID(default_value=uuid.uuid4())
    created_at = graphene.DateTime(default_value=datetime.now())
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()


class UserInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    password = graphene.String(required=True)


class CreateUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        user_data = UserInput(required=True)

    def mutate(self, info, user_data):
        user = User(username=user_data.username, email=user_data.email, password=user_data.password)
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=User, mutation=Mutation)
result = schema.execute("""
    mutation {
        createUser( userData:{
        username:"kevin",
        email:"kevin@email.com",
        password:"kevin123"
        } ){
            user{
                id
                createdAt
                username
                email       
            }
        }
    }
""")

j = json.dumps(result.data, indent=2)
print(j)
