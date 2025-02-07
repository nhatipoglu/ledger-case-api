from enum import Enum
from typing import Set

from api.schemas import BaseLedgerOperation, CoreLedgerOperation, validate_ledger_operations

class LedgerOperationType1(BaseLedgerOperation):
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"
    DAILY_REWARD = CoreLedgerOperation.DAILY_REWARD # Zorunlu operasyonlar
    SIGNUP_CREDIT = CoreLedgerOperation.SIGNUP_CREDIT
    CREDIT_SPEND = CoreLedgerOperation.CREDIT_SPEND
    CREDIT_ADD = CoreLedgerOperation.CREDIT_ADD

    @classmethod
    def required_operations(cls) -> Set['BaseLedgerOperation']:
       return set(CoreLedgerOperation)

validate_ledger_operations(LedgerOperationType1)

class LedgerOperationType2(BaseLedgerOperation):
    ITEM_PURCHASE = "ITEM_PURCHASE"
    ITEM_SALE = "ITEM_SALE"
    DAILY_REWARD = CoreLedgerOperation.DAILY_REWARD # Zorunlu operasyonlar
    SIGNUP_CREDIT = CoreLedgerOperation.SIGNUP_CREDIT
    CREDIT_SPEND = CoreLedgerOperation.CREDIT_SPEND
    CREDIT_ADD = CoreLedgerOperation.CREDIT_ADD

    @classmethod
    def required_operations(cls) -> Set['BaseLedgerOperation']:
       return set(CoreLedgerOperation)

validate_ledger_operations(LedgerOperationType2)