from datetime import date
from sqlalchemy import Column, String, Integer, Date

from database.entity import Entity, Base


class Report(Entity, Base):
    __tablename__ = 'reports'

    country = Column(String)
    province = Column(String)
    report = Column(Date)
    confirmed = Column(Integer)
    deaths = Column(Integer)
    recovered = Column(Integer)

    def __init__(self, country: str, province: str, report: str, confirmed: int, deaths: int, recovered: int):
        Entity.__init__(self)
        self.country = country
        self.province = province
        self.report = report
        self.confirmed = confirmed
        self.deaths = deaths
        self.recovered = recovered
