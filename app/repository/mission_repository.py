from datetime import date
from typing import List

from returns.maybe import Maybe

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
