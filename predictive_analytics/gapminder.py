from sqlalchemy import Column, String, Float, Integer
from entity import Entity, Base

class GapMinder(Entity, Base):
  __tablename__ = 'gapminder'

  country = Column(String)
  continent = Column(String)
  year = Column(Integer)
  life_expectancy = Column(Float)
  population = Column(Integer)
  gdp_per_capita = Column(Float)

  def __init__(self, country: str, continent: str, year: int, life_expectancy: float, population: int, gdp_per_capita: float):
    Entity.__init__(self)
    self.country = country
    self.continent = continent
    self.year = year
    self.life_expectancy = life_expectancy
    self.population = population
    self.gdp_per_capita = gdp_per_capita