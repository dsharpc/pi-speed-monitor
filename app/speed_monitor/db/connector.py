import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, SpeedMeasurement

def get_engine():
    user = os.getenv('PG_USER')
    password = os.getenv('PG_PASSWORD')
    host = os.getenv('PG_HOST')
    port = os.getenv('PG_PORT')
    db = os.getenv('PG_DATABASE')
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    return engine

def get_session(engine):
    Session = sessionmaker()
    Session.configure(bind=engine)
    ses = Session()
    return ses

def build_table():
    engine = get_engine()
    Base.metadata.create_all(engine)

def insert_to_db(obj: SpeedMeasurement):
    engine = get_engine()
    session = get_session(engine)
    session.add(obj)
    session.commit()

