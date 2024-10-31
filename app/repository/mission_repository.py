from returns.maybe import Maybe

from app.db.database import session_maker
from app.db.models import Mission


def get_mission_by_id(mission_id: int) -> Maybe[Mission]:
    with session_maker() as session:
        return Maybe.from_optional(session.query(Mission).filter_by(mission_id=mission_id).first())
