import logging

from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from api.exceptions import InsufficientBalance, DuplicateTransaction
from api.schemas import LedgerEntryResponse, BalanceResponse
from api.schemas.request_schemas import LedgerEntryRequest
from api.services.ledger_service import LedgerService

router = APIRouter(
    prefix="/ledger",
    tags=["Ledger Operations"],
    responses={404: {"description": "Not Found"}},
)


@router.get("/{owner_id}", response_model=BalanceResponse, status_code=200, summary="Get Account Balance",
            description="Kullanıcının mevcut bakiyesini döndürür.")
async def get_balance(owner_id: str):
    """
    **Kullanıcının bakiyesini döndürür.**

    - `owner_id`: Kullanıcının ID'si
    - **Başarılı Dönen Sonuç:**
    ```json
    {
        "success": true,
        "data": {
            "owner_id": "user123",
            "balance": 500
        }
    }
    ```
    """
    service = LedgerService()

    try:
        response = service.get_balance(owner_id)
        if not response.success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response.message)
        return JSONResponse(content=jsonable_encoder(response),
                            status_code=status.HTTP_201_CREATED)
    finally:
        service.close_db()


@router.post("/", response_model=LedgerEntryResponse, status_code=201, summary="Create Ledger Entry",
             description="Yeni bir Ledger girişi oluşturur.")
async def create_ledger_entry(request_body: LedgerEntryRequest):
    """
    **Yeni bir Ledger girişi oluşturur.**

    - `owner_id`: Kullanıcının ID'si
    - `operation`: İşlem türü (örneğin: `CREDIT_ADD`)
    - `amount`: İşlem miktarı
    - `nonce`: İşlem için benzersiz kimlik

    - **Başarılı Dönen Sonuç:**
    ```json
    {
        "success": true,
        "data": {
            "id": 12,
            "owner_id": "user123",
            "operation": "CREDIT_ADD",
            "amount": 10,
            "nonce": "abc123",
            "created_on": "2024-02-07T12:30:00"
        }
    }
    ```

    - **Başarısız Sonuç Örnekleri:**
        - **Yetersiz bakiye**
        ```json
        {
            "success": false,
            "message": "Yetersiz bakiye",
            "errors": ["InsufficientBalance"]
        }
        ```
        - **Tekrarlanan işlem**
        ```json
        {
            "success": false,
            "message": "Tekrarlanan işlem",
            "errors": ["DuplicateTransaction"]
        }
        ```
    """
    service = LedgerService()

    try:
        response = service.create_ledger_entry(
            request_body.owner_id,
            request_body.operation,
            request_body.amount,
            request_body.nonce
        )
        if not response.success:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response.message)
        JSONResponse(content=jsonable_encoder(response),
                     status_code=status.HTTP_201_CREATED if response.success else status.HTTP_400_BAD_REQUEST)
    except InsufficientBalance:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Yetersiz bakiye")
    except DuplicateTransaction:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Tekrarlanan işlem")
    finally:
        service.close_db()
