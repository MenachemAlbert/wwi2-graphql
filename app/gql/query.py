from graphene import ObjectType, Field, Int, List, Date, Argument, String

from app.gql.types.mission_type import MissionType
from app.repository.mission_repository import get_mission_by_id, get_mission_by_date_range, get_missions_by_county, \
    get_missions_by_target_industry


class Query(ObjectType):
    mission_by_id = Field(MissionType, mission_id=Int(required=True))
    mission_by_date_range = List(
        MissionType,
        start_date=Argument(Date, required=True),
        end_date=Argument(Date, required=True)
    )
    missions_by_county = List(MissionType, country=String(required=True))
    missions_by_target_industry = List(MissionType, target_industry=String(required=True))

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        return get_mission_by_id(mission_id).unwrap()

    @staticmethod
    def resolve_mission_by_date_range(root, info, start_date, end_date):
        return get_mission_by_date_range(start_date, end_date)

    @staticmethod
    def resolve_missions_by_county(root, info, country):
        return get_missions_by_county(country)

    @staticmethod
    def resolve_missions_by_target_industry(root, info, target_industry):
        return get_missions_by_target_industry(target_industry)
