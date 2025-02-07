from pydantic import BaseModel, Field, field_validator
from typing import Optional
from api.schemas.operation_schemas import BaseLedgerOperation

class TransferRequest(BaseModel):
    sender_id: str = Field(..., min_length=3, max_length=50, description="Gönderen kullanıcı ID'si")
    receiver_id: str = Field(..., min_length=3, max_length=50, description="Alıcı kullanıcı ID'si")
    amount: int = Field(..., gt=0, description="İşlem miktarı sıfırdan büyük olmalıdır")
    nonce: str = Field(..., min_length=5, max_length=50, description="İşlem kimliği en az 5 karakter olmalıdır")
    operation_type: Optional[str] = None

    @field_validator("sender_id", "receiver_id")
    def id_must_be_alphanumeric(cls, value):
        if not value.isalnum():
            raise ValueError("Kullanıcı ID sadece harf ve rakamlardan oluşmalıdır")
        return value

    @field_validator("nonce")
    def validate_nonce(cls, value):
        if len(value) < 5:
            raise ValueError("Nonce en az 5 karakter olmalıdır")
        return value

class LedgerEntryRequest(BaseModel):
    owner_id: str = Field(..., min_length=3, max_length=50, description="İşlem yapan kullanıcı ID'si")
    operation: BaseLedgerOperation
    amount: int = Field(..., gt=0, description="İşlem miktarı sıfırdan büyük olmalıdır")
    nonce: str = Field(..., min_length=5, max_length=50, description="Nonce en az 5 karakter olmalıdır")

    @field_validator("owner_id")
    def owner_id_must_be_valid(cls, value):
        if not value.isalnum():
            raise ValueError("Owner ID sadece harf ve rakam içermelidir")
        return value

    @field_validator("nonce")
    def nonce_must_be_unique(cls, value):
        if len(value) < 5:
            raise ValueError("Nonce en az 5 karakter olmalıdır")
        return value

    @field_validator("operation")
    def operation_must_be_valid(cls, value):
        if not isinstance(value, BaseLedgerOperation):
            raise ValueError("Geçersiz işlem türü")
        return value

class LedgerHistoryRequest(BaseModel):
    owner_id: str = Field(..., min_length=3, max_length=50, description="Kullanıcı ID'si")
    limit: int = Field(10, gt=0, le=100, description="En fazla 100 işlem gösterilebilir")
    offset: int = Field(0, ge=0, description="Başlangıç noktası en az 0 olmalıdır")
    operation_type: Optional[BaseLedgerOperation] = None

    @field_validator("owner_id")
    def owner_id_must_be_valid(cls, value):
        if not value.isalnum():
            raise ValueError("Owner ID sadece harf ve rakam içermelidir")
        return value
