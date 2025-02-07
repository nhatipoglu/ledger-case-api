from api.repository import LedgerRepository
from api.models import LedgerEntry
from api.schemas.operation_schemas import LedgerOperationType1, LedgerOperationType2
from api.schemas.response_schemas import LedgerEntryResponse, BalanceResponse

class LedgerService:
    def __init__(self):
        """Servis, kendi içinde repository'yi oluşturur."""
        self.repository = LedgerRepository()

    def close_db(self):
        """Bağlantıyı repository üzerinden kapatır."""
        self.repository.close_db()

    def get_balance(self, owner_id: str) -> BalanceResponse:
        """Kullanıcının bakiyesini döndürür."""
        existing_balance = self.repository.get_balance(owner_id)
        if existing_balance is None:
            return BalanceResponse(success=False, message="Kullanıcı bulunamadı", errors=["UserNotFound"])

        return BalanceResponse(success=True, data={"owner_id": owner_id, "balance": existing_balance})

    def create_ledger_entry(self, owner_id: str, operation, amount: int, nonce: str) -> LedgerEntryResponse:
        """Yeni bir ledger girişi oluşturur ve response modeliyle döner."""

        # Kullanıcının bakiyesi var mı kontrol et
        existing_balance = self.repository.get_balance(owner_id)
        if existing_balance is None:
            return LedgerEntryResponse(success=False, message="Kullanıcı bulunamadı", errors=["UserNotFound"])

        # Negatif işlem miktarlarını engelle
        if amount <= 0:
            return LedgerEntryResponse(success=False, message="İşlem miktarı sıfırdan büyük olmalıdır",
                                       errors=["InvalidAmount"])

        # Yetersiz bakiye kontrolü
        if existing_balance + amount < 0 and operation in [LedgerOperationType1.CREDIT_SPEND,
                                                           LedgerOperationType2.ITEM_PURCHASE]:
            return LedgerEntryResponse(success=False, message="Yetersiz bakiye", errors=["InsufficientBalance"])

        # Tekrarlanan işlem kontrolü
        if self.repository.get_entry_by_nonce(nonce):
            return LedgerEntryResponse(success=False, message="Tekrarlanan işlem", errors=["DuplicateTransaction"])

        # Yeni işlem ekle
        entry = LedgerEntry(owner_id=owner_id, operation=operation, amount=amount, nonce=nonce)
        entry = self.repository.add_entry(entry)

        return LedgerEntryResponse(
            success=True,
            data={
                "id": entry.id,
                "owner_id": entry.owner_id,
                "operation": entry.operation,
                "amount": entry.amount,
                "nonce": entry.nonce,
                "created_on": entry.created_on
            }
        )
