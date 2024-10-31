from graphene import ObjectType, Field, Int, List, Date, Argument

from app.gql.types.mission_type import MissionType
from app.repository.mission_repository import get_mission_by_id, get_mission_by_date_range


class Query(ObjectType):
    mission_by_id = Field(MissionType, mission_id=Int())
    mission_by_date_range = List(
        MissionType,
        start_date=Argument(Date, required=True),
        end_date=Argument(Date, required=True)
    )

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        return get_mission_by_id(mission_id).unwrap()

    @staticmethod
    def resolve_mission_by_date_range(root, info, start_date, end_date):
        return get_mission_by_date_range(start_date, end_date)
