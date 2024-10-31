from sqlalchemy import Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.orm import relationship

from app.db.models import Base


class Target(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, Sequence('target_id_seq'), primary_key=True)
    target_industry = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey('cities.city_id'), nullable=False)
    mission_id = Column(Integer, ForeignKey('missions.mission_id'), nullable=False)
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'), nullable=True)
    target_priority = Column(Integer, nullable=False)

    city = relationship("City", back_populates="targets")
    mission = relationship('Mission')
    target_type = relationship("TargetType", back_populates="targets")


