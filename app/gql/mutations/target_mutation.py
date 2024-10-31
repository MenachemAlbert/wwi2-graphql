from graphene import Mutation, Int, String, Field
from returns.result import Success

from app.db.models import Target
from app.gql.types.target_type import TargetType
from app.repository.target_repository import create_target


class AddTarget(Mutation):
    class Arguments:
        mission_id = Int(required=True)
        target_industry = String(required=True)
        city_id = Int(required=True)
        target_type_id = Int(required=True)
        target_priority = Int(required=True)

    target = Field(lambda: TargetType)

    @staticmethod
    def mutate(root, info, mission_id, target_industry, city_id, target_type_id, target_priority):
        target_to_add = Target(mission_id=mission_id, target_industry=target_industry,
                               city_id=city_id, target_type_id=target_type_id, target_priority=target_priority)
        new_target = create_target(target_to_add)
        if isinstance(new_target, Success):
            return AddTarget(target=new_target.unwrap())
        else:
            raise Exception("can`t create target")



