import pandas
import numpy

from entity import Session, engine, Base
from countries import Country
from continents import Continent

session = Session()


def get_continent_by(name):
    return session.query(Continent).filter_by(continent=name).first()


def get_country_by(name):
    return session.query(Country).filter_by(country=name).first()


def add_continent(continent: str):
    session.add(Continent(continent))
    session.commit()


def add_country(country: str, continent_id: int):
    session.add(Country(country, continent_id))
    session.commit()


def create_catalogs(gapminder):
    Base.metadata.create_all(engine)

    for continent in gapminder['continent'].drop_duplicates().values.tolist():
        add_continent(continent)

    for country, continent in gapminder[['country', 'continent']].drop_duplicates(subset='country').values.tolist():
        continent_id = get_continent_by(continent).id
        add_country(country, continent_id)
