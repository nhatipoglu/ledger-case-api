# config/operation_config.py
from api.schemas import CoreLedgerOperation

LEDGER_OPERATION_CONFIG = {
    CoreLedgerOperation.DAILY_REWARD: 1,
    CoreLedgerOperation.SIGNUP_CREDIT: 3,
    CoreLedgerOperation.CREDIT_SPEND: -1,
    CoreLedgerOperation.CREDIT_ADD: 10,
}

def get_operation_value(operation):
    """Belirtilen operasyonun değerini döndürür, yoksa 0 döner."""
    return LEDGER_OPERATION_CONFIG.get(operation, 0)
