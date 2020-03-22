from database.entity import Session, engine, Base
from database.reports import Report

Base.metadata.create_all(engine)
session = Session()


def get_query():
    return session.query(Report)


def add_report(country: str, province: str, report: str, confirmed: int, deaths: int, recovered: int):
    session.add(
        Report(
            country,
            province,
            report,
            confirmed,
            deaths,
            recovered,
        )
    )
    session.commit()
