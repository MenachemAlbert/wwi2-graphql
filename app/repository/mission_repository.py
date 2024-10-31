from datetime import date
from typing import List

from graphql import GraphQLError
from returns.maybe import Maybe
from returns.result import Success, Failure
from sqlalchemy import func

from app.db.database import session_maker
from app.db.models import Mission, Country, Target, City, TargetType


def get_mission_by_id(mission_id: int) -> Maybe[Mission]:
    with session_maker() as session:
        return Maybe.from_optional(session.query(Mission).filter_by(mission_id=mission_id).first())


def get_mission_by_date_range(start_date: date, end_date: date) -> List[Mission]:
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_date.between(start_date, end_date)).all()


def get_missions_by_county(country: str) -> List[Mission]:
    with session_maker() as session:
        return (session.query(Mission)
                .join(Mission.targets)
                .join(Target.city)
                .join(City.country).filter(Country.country_name == country).all())


def get_missions_by_target_industry(target_industry: str) -> List[Mission]:
    with session_maker() as session:
        return (session.query(Mission)
                .join(Mission.targets)
                .filter(Target.target_industry == target_industry).all())


def get_missions_by_target_type(target_type: str) -> List[Mission]:
    with session_maker() as session:
        return (session.query(Mission)
                .join(Mission.targets)
                .join(Target.target_type)
                .filter(TargetType.target_type_name == target_type).all())


def create_mission(mission: Mission) -> Maybe[Mission]:
    with session_maker() as session:
        try:
            max_id = session.query(func.max(Mission.mission_id)).scalar()
            new_id = (max_id or 0) + 1
            mission.mission_id = new_id
            session.add(mission)
            session.commit()
            session.refresh(mission)
            return Success(mission)
        except GraphQLError as e:
            session.rollback()
            return Failure(str(e))
