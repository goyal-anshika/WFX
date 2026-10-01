from fastapi import FastAPI

from app.routes import buyers
from app.routes import suppliers
from app.routes import finished_goods
from app.routes import tech_packs
from app.routes import sales_orders
from app.routes import sales_invoices

from app.routes.search import router as search_router

from app.routes.ai import router as ai_router

from app.routes.image_search import router as image_search_router

from app.routes.dashboard import router as dashboard_router

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="WFX Backend API",
    description="Backend API for the WFX project",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(buyers.router)
app.include_router(suppliers.router)
app.include_router(finished_goods.router)
app.include_router(tech_packs.router)
app.include_router(sales_orders.router)
app.include_router(sales_invoices.router)

app.include_router(search_router)

app.include_router(ai_router)

app.include_router(image_search_router)

app.include_router(dashboard_router)

@app.get("/")
def root():
    return {
        "message": "WFX Backend API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }