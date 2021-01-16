"""models.py
Database ORM models using SQLAlchemy
"""
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SpeedMeasurement(Base):
    __tablename__ = 'speed_measurements'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    download = Column(Float)
    bytes_received = Column(Float)
    upload = Column(Float)
    bytes_sent = Column(Float)
    ping = Column(Float)
    server_url = Column(String)
    server_name = Column(String)
    server_country = Column(String)
    server_sponsor = Column(String)
    server_host = Column(String)
    client_isp = Column(String)
    client_isprating = Column(String)
