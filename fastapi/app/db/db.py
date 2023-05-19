from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Sequence
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.sql import func
from datetime import datetime
from app import config

settings = config.get_postgres_settings()
SQLALCHEMY_DATABASE_URI_POSTGRES = f'postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}/{settings.POSTGRES_DB_NAME}'
engine = create_engine(SQLALCHEMY_DATABASE_URI_POSTGRES)
sessionLocal = sessionmaker(autocommit = False, autoflush=False, bind = engine)
Base  = declarative_base()

USER_ID_SEQ = Sequence('user_id_seq')

class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, USER_ID_SEQ, primary_key = True, server_default=USER_ID_SEQ.next_value())
    email = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    password = Column(String, nullable=False)
    time_created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    time_updated = Column(TIMESTAMP(timezone=True), onupdate=text('now()'))

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()