import csv

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

def add_row(country, continent, year, life_expectancy, population, gdp_per_capita):
  session.add(GapMinder(country, continent, year, life_expectancy, population, gdp_per_capita))
  session.commit()

with open('gapminder.csv') as datafile:
  reader = csv.DictReader(datafile)
  for row in reader:
    add_row(row['country'], row['continent'], row['year'], row['lifeExp'], row['pop'], row['gdpPercap'])

print(get_all())