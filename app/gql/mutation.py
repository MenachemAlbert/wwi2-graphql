from graphene import ObjectType

from app.gql.mutations.mission_mutation import AddMission
from app.gql.mutations.target_mutation import AddTarget


class Mutation(ObjectType):
    create_mission = AddMission.Field()
    create_target = AddTarget.Field()


