from sqlalchemy import Column, String, Integer
from entity import Entity, Base


class Country(Entity, Base):
    __tablename__ = 'countries'

    country = Column(String)
    continent_id = Column(Integer)

    def __init__(self, country: str, continent_id: int):
        Entity.__init__(self)
        self.country = country
        self.continent_id = continent_id
