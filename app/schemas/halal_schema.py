from pydantic import BaseModel

class IngredientAnalysis(BaseModel):
    ingredient: str
    is_halal: str
    reason: str
    confidence: int
    evidence: list[dict] = []

class HalalAnalysisResponse(BaseModel):
    product_name: str
    category: str
    is_edible: bool
    is_halal: str
    ingredients_analysis: list[IngredientAnalysis]
    overall_summary: str
    google_evidence_used: bool

class ProductInput(BaseModel):
    text: str | None = None
    product_name: str | None = None
    category: str | None = None
    ingredients: list[str] | None = None

