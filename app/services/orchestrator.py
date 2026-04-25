from app.services.gemini_service import GeminiService
from app.services.search_service import FreeSearchService
from app.schemas.halal_schema import IngredientAnalysis

class Orchestrator:
    def __init__(self):
        self.gemini = GeminiService()
        self.search = FreeSearchService()

    async def analyze_product(self, text: str) -> dict:
        """Main orchestration flow"""

        # Step 1: Classification
        classification = self.gemini.classify_product(text)
        product_name = classification.get("product_name", "Unknown")
        category = classification.get("category", "other")
        is_edible = classification.get("is_edible", False)

        # Step 2: Early return if not edible
        if not is_edible:
            return {
                "product_name": product_name,
                "category": category,
                "is_edible": False,
                "is_halal": "doubtful",
                "ingredients_analysis": [],
                "overall_summary": "Mahsulot iste'mol qilinmaydi, halal tekshiruvi qo'llanilmaydi",
                "google_evidence_used": False
            }

        # Step 3: Extract ingredients
        ingredients = self.gemini.extract_ingredients(text)

        # Step 4: Analyze each ingredient
        ingredients_analysis = []
        google_evidence_used = False

        for ingredient in ingredients:
            # Gemini analysis
            ingredient_analysis = self.gemini.analyze_ingredient(ingredient)

            # Search for evidence
            search_results = await self.search.search_ingredient(ingredient)

            if search_results:
                google_evidence_used = True

            ingredients_analysis.append(IngredientAnalysis(
                ingredient=ingredient,
                is_halal=ingredient_analysis.get("is_halal", "doubtful"),
                reason=ingredient_analysis.get("reason", "Noma'lum"),
                confidence=ingredient_analysis.get("confidence", 50),
                evidence=[
                    {"title": r.get("title"), "link": r.get("link")}
                    for r in search_results[:2]
                ]
            ))

        # Step 5: Determine final halal status
        is_halal = self._determine_halal_status(ingredients_analysis)

        # Step 6: Generate summary
        overall_summary = self._generate_summary(product_name, category, is_halal, ingredients_analysis)

        return {
            "product_name": product_name,
            "category": category,
            "is_edible": is_edible,
            "is_halal": is_halal,
            "ingredients_analysis": ingredients_analysis,
            "overall_summary": overall_summary,
            "google_evidence_used": google_evidence_used
        }

    def _determine_halal_status(self, ingredients_analysis: list[IngredientAnalysis]) -> str:
        """Merge engine logic"""
        if not ingredients_analysis:
            return "true"

        # If any ingredient is false (haram), entire product is false
        if any(item.is_halal == "false" for item in ingredients_analysis):
            return "false"

        # If any ingredient is doubtful, entire product is doubtful
        if any(item.is_halal == "doubtful" for item in ingredients_analysis):
            return "doubtful"

        return "true"

    def _generate_summary(self, product_name: str, category: str, is_halal: str, ingredients: list) -> str:
        """Generate Uzbek summary"""
        summary = f"Mahsulot '{product_name}' ({category}). "
        summary += f"Halal holati: {is_halal}. "

        if ingredients:
            summary += f"{len(ingredients)} ta ingredient tahlil qilindi. "

            haram_count = sum(1 for i in ingredients if i.is_halal == "false")
            doubtful_count = sum(1 for i in ingredients if i.is_halal == "doubtful")

            if haram_count > 0:
                summary += f"{haram_count} ta harom ingredient topildi. "
            if doubtful_count > 0:
                summary += f"{doubtful_count} ta shubhali ingredient topildi."

        return summary

