import pandas
import numpy

from entity import Session, engine, Base
from gapminder import GapMinder
from catalogs import create_catalogs, get_country_by

Base.metadata.create_all(engine)
session = Session()


def get_query():
    return session.query(GapMinder)


def get_row_by(id):
    return get_query().filter_by(id=id).first()


def add_row(country_id: int, year: int, life_expectancy: float, population: int, gdp_per_capita: float):
    session.add(
        GapMinder(
            country_id,
            year, life_expectancy,
            population, gdp_per_capita
        )
    )
    session.commit()


gapminder = pandas.read_csv('gapminder.csv', dtype={
    'year': numpy.int64,
    'life_expectancy': numpy.float64,
    'population': numpy.int64,
    'gdp_per_capita': numpy.float64
})

create_catalogs(gapminder)

for index, row in gapminder.iterrows():
    country_id = get_country_by(row['country']).id
    add_row(
        country_id,
        row['year'],
        row['lifeExp'],
        row['pop'],
        row['gdpPercap']
    )
