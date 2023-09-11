
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .database import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    type = Column(String)
    counter = Column(Float)
    measure = Column(Float)
    measuretype = Column(String)
    owner_id = Column(Integer, ForeignKey("properties.id"))

    owner = relationship("Property", back_populates="measurements")



