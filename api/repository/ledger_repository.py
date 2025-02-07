from sqlalchemy import func
from sqlalchemy.orm import Session

from api.db_manager.database import SessionLocal
from api.models import LedgerEntry


class LedgerRepository:
    def __init__(self):
        """Veritabanı bağlantısını açar."""
        self.db: Session = SessionLocal()

    def close_db(self):
        """Bağlantıyı kapatır."""
        self.db.close()

    def get_balance(self, owner_id: str) -> int:
        balance = self.db.query(func.sum(LedgerEntry.amount)).filter(LedgerEntry.owner_id == owner_id).scalar()
        return balance or 0

    def get_entry_by_nonce(self, nonce: str):
        return self.db.query(LedgerEntry).filter(LedgerEntry.nonce == nonce).first()

    def add_entry(self, entry: LedgerEntry):
        self.db.add(entry)
        self.db.commit()
        self.db.refresh(entry)
        return entry
