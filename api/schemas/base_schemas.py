from enum import Enum
from typing import Set

class BaseLedgerOperation(Enum):
    """Ledger Operasyonları için Temel Sınıf. Alt sınıflar tarafından genişletilmelidir."""
    pass

    @classmethod
    def required_operations(cls) -> Set['BaseLedgerOperation']:
        """Alt sınıflarda *olması gereken* operasyonları döndürür."""
        return set()

class CoreLedgerOperation(BaseLedgerOperation):
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"

    @classmethod
    def required_operations(cls) -> Set['BaseLedgerOperation']:
        return set(cls)

def validate_ledger_operations(operations_class: type[BaseLedgerOperation]):
    required = operations_class.required_operations()
    for op in CoreLedgerOperation:
        if op not in required:
            raise ValueError(f"Gerekli operasyon {op}, {operations_class.__name__} içinde eksik")