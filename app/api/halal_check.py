from fastapi import APIRouter, HTTPException
from app.schemas.halal_schema import ProductInput, HalalAnalysisResponse
from app.services.orchestrator import Orchestrator

router = APIRouter(prefix="/api/v1", tags=["halal_check"])
orchestrator = Orchestrator()

@router.post("/analyze", response_model=dict)
async def analyze_product(product: ProductInput) -> dict:
    """Analyze product for Halal compliance"""

    if not product.text and not product.product_name:
        raise HTTPException(status_code=400, detail="text or product_name required")

    text = product.text or product.product_name

    result = await orchestrator.analyze_product(text)
    return result

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "service": "halal-analyzer"}

