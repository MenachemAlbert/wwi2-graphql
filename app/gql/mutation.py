from graphene import ObjectType

from app.gql.mutations.mission_mutation import AddMission


class Mutation(ObjectType):
    create_mission = AddMission.Field()

