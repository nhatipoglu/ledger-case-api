from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from api.config import Config

DATABASE_URL = Config.DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    pool_size=10,  # Maksimum bağlantı sayısı
    max_overflow=20,  # Fazladan izin verilen bağlantılar
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
