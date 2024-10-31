from graphene import ObjectType, Field, Int

from app.gql.types.mission_type import MissionType
from app.repository.mission_repository import get_mission_by_id


class Query(ObjectType):
    mission_by_id = Field(MissionType, mission_id=Int())

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        return get_mission_by_id(mission_id).unwrap()
