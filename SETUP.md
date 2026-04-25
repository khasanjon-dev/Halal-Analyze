# PRODUCTION SETUP GUIDE

## 🚀 Quick Start

### 1. Environment Setup
```bash
# Copy example to .env
cp .env.example .env

# Edit .env and add your GEMINI_API_KEY
export GEMINI_API_KEY="your_actual_api_key_here"
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Server
```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Test API
```bash
# Health check
curl http://localhost:8000/api/v1/health

# Analyze product
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "text": "chocolate with gelatin"
  }'
```

## 📊 System Architecture

```
USER REQUEST
    ↓
FastAPI Endpoint (/api/v1/analyze)
    ↓
Orchestrator (Decision Engine)
    ├── Gemini Service
    │   ├── classify_product()     → Extract category + is_edible
    │   ├── extract_ingredients()  → Get list of ingredients
    │   └── analyze_ingredient()   → Analyze each ingredient
    ├── Search Service
    │   └── search_ingredient()    → Get evidence from web
    └── Merge Logic
        ├── If false → false (HARAM)
        ├── If doubtful → doubtful
        └── Else → true (HALAL)
    ↓
JSON Response (Uzbek)
```

## 🧠 Key Services

### GeminiService (app/services/gemini_service.py)
- **classify_product()** - Determines category (food/drink/cosmetic/etc) and edibility
- **extract_ingredients()** - Extracts ingredient list from product description
- **analyze_ingredient()** - Analyzes individual ingredient halal status

### FreeSearchService (app/services/search_service.py)
- **search()** - Generic DuckDuckGo search
- **search_ingredient()** - Search halal/haram info for ingredient
- **search_product()** - Search certification info for product

### Orchestrator (app/services/orchestrator.py)
- **analyze_product()** - Main flow controller
- **_determine_halal_status()** - Merge engine logic
- **_generate_summary()** - Create Uzbek summary

## 📝 API Response Format

```json
{
  "product_name": "Chocolate",
  "category": "food",
  "is_edible": true,
  "is_halal": "true|false|doubtful",
  "ingredients_analysis": [
    {
      "ingredient": "gelatin",
      "is_halal": "doubtful",
      "reason": "jelatin manbasi noma'lum",
      "confidence": 80,
      "evidence": [
        {
          "title": "Search result title",
          "link": "https://..."
        }
      ]
    }
  ],
  "overall_summary": "Uzbek language summary",
  "google_evidence_used": true
}
```

## 🔧 Configuration

Edit `.env` file:
```
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3-flash-preview
DEBUG=False
HOST=0.0.0.0
PORT=8000
```

## 📚 Documentation

- **Interactive Docs**: http://localhost:8000/docs (Swagger UI)
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/api/v1/health

## 🔒 Production Deployment

For production, update `app/main.py`:
```python
uvicorn.run(
    "app.main:app",
    host=settings.HOST,
    port=settings.PORT,
    reload=False,  # Disable reload in production
    workers=4      # Use multiple workers
)
```

Or use with Gunicorn:
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

## 📦 Dependencies

- **FastAPI** - Web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **google-generativeai** - Gemini API client
- **beautifulsoup4** - HTML parsing
- **httpx** - Async HTTP client

---

**Status**: ✅ Production Ready

