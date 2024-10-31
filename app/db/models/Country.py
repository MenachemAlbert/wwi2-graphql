from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship

from app.db.models import Base


class Country(Base):
    __tablename__ = "countries"
    country_id = Column(Integer, Sequence('country_id_seq'), primary_key=True)
    country_name = Column(String, unique=True, nullable=False)

    cities = relationship("City", back_populates="country", lazy="joined")


