from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship

from app.db.models import Base


class TargetType(Base):
    __tablename__ = 'targettypes'
    target_type_id = Column(Integer, Sequence('target_type_id_seq'), primary_key=True)
    target_type_name = Column(String, unique=True, nullable=False)

    targets = relationship("Target", back_populates="target_type", lazy="joined")


