import webbrowser

import uvicorn
from fastapi import FastAPI
from api.routes.ledger_routes import router as ledger_router

app = FastAPI(
    title="Ledger API",
    description="Kullanıcıların bakiyelerini yönettiği ve işlemler gerçekleştirdiği API servisi.",
    version="0.0.1",
    docs_url="/api/swagger",
    redoc_url="/api/redoc",
)

app.include_router(ledger_router)



if __name__ == "__main__":

    uvicorn.run(app="api.main:app", host="0.0.0.0", port=5200, reload=True, log_level="info")
    webbrowser.open("http://localhost:5200/api/swagger")

