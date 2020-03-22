from sqlalchemy import Column, String, Boolean, Integer
from entity import Entity, Base

class GapMinder(Entity, Base):
  __tablename__ = 'gapminder'

  country = Column(String)
  continent = Column(String)
  year = Column(Integer)
  life_expectancy = Column(Integer)
  population = Column(Integer)
  gdp_per_capita = Column(Integer)

  def __init__(self, country, continent, year, life_expectancy, population, gdp_per_capita):
    Entity.__init__(self)
    self.country = country
    self.continent = continent
    self.year = year
    self.life_expectancy = life_expectancy
    self.population = population
    self.gdp_per_capita = gdp_per_capita