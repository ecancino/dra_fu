import pandas
import numpy

from entity import Session, engine, Base
from gapminder import GapMinder

Base.metadata.create_all(engine)
session = Session()

def get_query():
  return session.query(GapMinder)

def get_row_by(id):
  return get_query().filter_by(id=id).first()

def get_all():
  return get_query().all()

def add_row(country: str, continent: str, year: int, life_expectancy: float, population: int, gdp_per_capita: float):
  session.add(GapMinder(country, continent, year, life_expectancy, population, gdp_per_capita))
  session.commit()

gapminder = pandas.read_csv('gapminder.csv', dtype = {
  'year': numpy.int64,
  'life_expectancy': numpy.float64,
  'population': numpy.int64,
  'gdp_per_capita': numpy.float64
})

for index, row in gapminder.iterrows():
  add_row(row['country'], row['continent'], row['year'], row['lifeExp'], row['pop'], row['gdpPercap'])

# print(gapminder)