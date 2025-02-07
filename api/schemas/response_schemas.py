from pydantic import BaseModel
from typing import Optional, Union, List
from datetime import datetime
from api.schemas.operation_schemas import BaseLedgerOperation

class BaseResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    errors: Optional[List[str]] = None

class LedgerEntryResponse(BaseResponse):
    data: Optional[dict] = None

class BalanceResponse(BaseResponse):
    data: Optional[dict] = None
