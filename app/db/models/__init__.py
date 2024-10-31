from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .Country import Country
from .City import City
from .TargetType import TargetType
from .Mission import Mission
from .Target import Target
