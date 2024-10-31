from datetime import date
from typing import List

from returns.maybe import Maybe
from sqlalchemy import and_

from app.db.database import session_maker
from app.db.models import Mission


def get_mission_by_id(mission_id: int) -> Maybe[Mission]:
    with session_maker() as session:
        return Maybe.from_optional(session.query(Mission).filter_by(mission_id=mission_id).first())


def get_mission_by_date_range(start_date: date, end_date: date) -> List[Mission]:
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_date.between(start_date, end_date)).all()
