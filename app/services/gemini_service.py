import google.generativeai as genai
import json
from app.core.config import settings

class GeminiService:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(settings.GEMINI_MODEL)

    def classify_product(self, text: str) -> dict:
        """Classify product and determine if edible"""
        prompt = f"""
        Uzbek tilida o'zbek tilidagi mahsulot: "{text}"
        
        Faqat JSON formatida javob ber:
        {{
            "category": "food|drink|supplement|cosmetic|medicine|book|electronics|other",
            "is_edible": true/false,
            "product_name": "string"
        }}
        
        Klassifikatsiya qoidalari:
        - food, drink, supplement → is_edible = true
        - cosmetic, medicine, book, electronics → is_edible = false
        """
        response = self.model.generate_content(prompt)
        try:
            return json.loads(response.text)
        except:
            return {
                "category": "other",
                "is_edible": False,
                "product_name": text
            }

    def extract_ingredients(self, text: str) -> list[str]:
        """Extract ingredients from product text"""
        prompt = f"""
        Mahsulotdan ingredientlarni ajrat: "{text}"
        
        Faqat JSON formatida javob ber:
        {{
            "ingredients": ["ingredient1", "ingredient2", ...]
        }}
        
        Qoidalar:
        - Har bir ingredientni alohida qatorga yoz
        - Kichik harflar bilan yoz
        - Tekrorlash yo'q
        - Agar ingredient bo'lmasa: []
        """
        response = self.model.generate_content(prompt)
        try:
            data = json.loads(response.text)
            return data.get("ingredients", [])
        except:
            return []

    def analyze_ingredient(self, ingredient: str) -> dict:
        """Analyze single ingredient for halal status"""
        prompt = f"""
        Ingredient: "{ingredient}"
        
        Uzbek tilida faqat JSON formatida javob ber:
        {{
            "is_halal": "true|false|doubtful",
            "reason": "o'zbek tilida tushuntirish",
            "confidence": 0-100
        }}
        
        Qoidalar:
        - Pork, alcohol, gelatin → false
        - Noma'lum manba → doubtful
        - O'simlik/tabiiy → true
        """
        response = self.model.generate_content(prompt)
        try:
            return json.loads(response.text)
        except:
            return {
                "is_halal": "doubtful",
                "reason": "Tahlil mumkin emas",
                "confidence": 30
            }

