from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://ravindu_sit722_postgresql_0nfp_user:Olo8Q4msmzItCh0AQVlUy1eqgzmDZnhW@dpg-crjrckjtq21c73a598h0-a.oregon-postgres.render.com/ravindu_sit722_postgresql_0nfp" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
