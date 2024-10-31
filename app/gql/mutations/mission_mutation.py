from graphene import Mutation, Date, Float, Field, Int, Boolean, String
from graphql import GraphQLError
from returns.result import Success

from app.db.models import Mission
from app.gql.types.mission_type import MissionType
from app.repository.mission_repository import create_mission, delete_mission


class AddMission(Mutation):
    class Arguments:
        mission_date = Date(required=True)
        airborne_aircraft = Float(required=True)
        attacking_aircraft = Float(required=True)
        bombing_aircraft = Float(required=True)
        aircraft_returned = Float(required=True)
        aircraft_failed = Float(required=True)
        aircraft_damaged = Float(required=True)
        aircraft_lost = Float(required=True)

    mission = Field(lambda: MissionType)

    @staticmethod
    def mutate(root, info, mission_date, airborne_aircraft, attacking_aircraft, bombing_aircraft, aircraft_returned,
               aircraft_failed, aircraft_damaged, aircraft_lost):
        mission_to_add = Mission(mission_date=mission_date, airborne_aircraft=airborne_aircraft,
                                 attacking_aircraft=attacking_aircraft,
                                 bombing_aircraft=bombing_aircraft, aircraft_returned=aircraft_returned,
                                 aircraft_failed=aircraft_failed,
                                 aircraft_damaged=aircraft_damaged, aircraft_lost=aircraft_lost)
        new_mission = create_mission(mission_to_add)
        if isinstance(new_mission, Success):
            return AddMission(mission=new_mission.unwrap())
        else:
            raise Exception("can`t create mission")


class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int()

    result = Field(Boolean)
    message = Field(String)

    @staticmethod
    def mutate(root, info, mission_id):
        result = delete_mission(mission_id)

        return DeleteMission(result=True if isinstance(result, Success) else False, message=str(result))
