from graphql import GraphQLError
from returns.maybe import Maybe
from returns.result import Success, Failure
from sqlalchemy import func

from app.db.database import session_maker
from app.db.models import Target, Mission


def create_target(target: Target) -> Maybe[Target]:
    with session_maker() as session:
        try:
            mission = session.query(Mission).filter(Mission.mission_id == target.mission_id).first()
            if not mission:
                raise GraphQLError("mission not found")
            max_id = session.query(func.max(Target.target_id)).scalar()
            new_id = (max_id or 0) + 1
            target.target_id = new_id
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
        except GraphQLError as e:
            session.rollback()
            return Failure(str(e))
