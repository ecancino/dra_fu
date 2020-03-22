from sqlalchemy import Column, String
from entity import Entity, Base


class Continent(Entity, Base):
    __tablename__ = 'continents'

    continent = Column(String)

    def __init__(self, continent: str):
        Entity.__init__(self)
        self.continent = continent
