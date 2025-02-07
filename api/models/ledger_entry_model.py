from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
import datetime
from api.schemas import BaseLedgerOperation

Base = declarative_base()

class LedgerEntry(Base):
    __tablename__ = "ledger_entries"

    id = Column(Integer, primary_key=True)
    operation = Column(Enum(BaseLedgerOperation), nullable=False)
    amount = Column(Integer, nullable=False)
    nonce = Column(String, nullable=False, unique=True)
    owner_id = Column(String, nullable=False)
    created_on = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)