#!/bin/bash

cat << 'EOF'

╔══════════════════════════════════════════════════════════════╗
║           HALAL ANALYZER - PRODUCTION BUILD              ║
║               STATUS: ✅ READY FOR DEPLOYMENT              ║
╚══════════════════════════════════════════════════════════════╝

PROJECT OVERVIEW
════════════════════════════════════════════════════════════════

Halal Analyzer is a production-ready AI system that:
  ✓ Classifies products into 8 categories
  ✓ Extracts ingredients using Gemini 3 Flash Preview
  ✓ Analyzes halal status with AI + web evidence
  ✓ Returns structured JSON in Uzbek language
  ✓ Provides confidence scores & evidence links

BUILD MANIFEST
════════════════════════════════════════════════════════════════

Core Application Files:
  ✓ app/main.py                 - FastAPI entry point
  ✓ app/core/config.py          - Configuration management
  ✓ app/services/gemini_service.py    - Gemini AI integration
  ✓ app/services/search_service.py    - Web search (DuckDuckGo)
  ✓ app/services/orchestrator.py      - Main orchestration engine
  ✓ app/api/halal_check.py            - API endpoints
  ✓ app/schemas/halal_schema.py       - Pydantic models

Configuration:
  ✓ requirements.txt            - Python dependencies
  ✓ .env.example                - Configuration template
  ✓ setup.sh                    - Quick setup script

Documentation:
  ✓ AGENTS.md                   - Architecture specification
  ✓ README.md                   - API documentation
  ✓ SETUP.md                    - Production setup guide
  ✓ MANIFEST.md                 - Detailed file manifest

ARCHITECTURE
════════════════════════════════════════════════════════════════

                    FastAPI Application
                           │
              ┌────────────┼────────────┐
              │            │            │
        GeminiService  SearchService  Orchestrator
              │            │            │
              └────────────┼────────────┘
                           │
                    JSON Response
                      (Uzbek)

DATA FLOW
════════════════════════════════════════════════════════════════

Input: { "text": "chocolate with gelatin" }
  ↓
1. Classify → { category: "food", is_edible: true }
  ↓
2. Extract Ingredients → ["chocolate", "gelatin"]
  ↓
3. For Each Ingredient:
   ├── Gemini Analysis (halal status)
   ├── Web Search (evidence)
   └── Merge Results
  ↓
4. Determine Status:
   ├── If any "false" → "false" (HARAM)
   ├── Else if any "doubtful" → "doubtful"
   └── Else → "true" (HALAL)
  ↓
5. Generate Uzbek Summary
  ↓
Output: Full JSON Report

API ENDPOINTS
════════════════════════════════════════════════════════════════

POST /api/v1/analyze
  • Main analysis endpoint
  • Input: { "text": "product description" }
  • Output: Full halal analysis JSON

GET /api/v1/health
  • Health check
  • Output: { "status": "ok" }

GET /docs
  • Swagger UI (interactive API testing)

GET /redoc
  • ReDoc documentation

REQUIRED CONFIGURATION
════════════════════════════════════════════════════════════════

1. Create .env file:
   cp .env.example .env

2. Add Gemini API Key:
   GEMINI_API_KEY=your_actual_key_here

3. Keep model as:
   GEMINI_MODEL=gemini-3-flash-preview

GETTING STARTED
════════════════════════════════════════════════════════════════

Step 1: Setup
  $ cp .env.example .env
  $ # Edit .env with your GEMINI_API_KEY
  $ pip install -r requirements.txt

Step 2: Run Server
  $ python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Step 3: Test API
  $ curl -X POST http://localhost:8000/api/v1/analyze \
      -H "Content-Type: application/json" \
      -d '{"text": "chocolate with nuts"}'

Step 4: Access Documentation
  • Swagger UI: http://localhost:8000/docs
  • ReDoc: http://localhost:8000/redoc

RESPONSE FORMAT
════════════════════════════════════════════════════════════════

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
          "title": "Search result",
          "link": "https://..."
        }
      ]
    }
  ],
  "overall_summary": "Uzbek language summary",
  "google_evidence_used": true
}

DEPENDENCIES
════════════════════════════════════════════════════════════════

Core Framework:
  • FastAPI 0.104.1        - Web framework
  • Uvicorn 0.24.0         - ASGI server
  • Pydantic 2.5.0         - Data validation
  • Pydantic-Settings 2.1  - Config management

AI & Search:
  • google-generativeai 0.3.0  - Gemini API
  • beautifulsoup4 4.12.2      - HTML parsing
  • httpx 0.25.2               - Async HTTP

Database (Optional):
  • SQLAlchemy 2.0.23      - ORM

Utilities:
  • python-dotenv 1.0.0    - Environment variables
  • requests 2.31.0        - HTTP requests

SERVICE DETAILS
════════════════════════════════════════════════════════════════

GeminiService:
  • classify_product()        - Category + edibility check
  • extract_ingredients()     - Get ingredient list
  • analyze_ingredient()      - Halal status analysis

FreeSearchService:
  • search()                  - Generic DuckDuckGo search
  • search_ingredient()       - Ingredient-specific search
  • search_product()          - Product certification search

Orchestrator:
  • analyze_product()         - Main orchestration flow
  • _determine_halal_status() - Merge logic engine
  • _generate_summary()       - Uzbek text generation

PRODUCTION DEPLOYMENT
════════════════════════════════════════════════════════════════

With Gunicorn:
  $ gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app

With Docker:
  FROM python:3.12
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY app/ app/
  CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

Environment Variables:
  • GEMINI_API_KEY       - Your Gemini API key (required)
  • GEMINI_MODEL         - gemini-3-flash-preview (default)
  • DEBUG                - False for production
  • HOST                 - 0.0.0.0 (default)
  • PORT                 - 8000 (default)

CODE QUALITY
════════════════════════════════════════════════════════════════

✓ Type hints throughout
✓ Comprehensive docstrings
✓ Async/await patterns
✓ Error handling with HTTPException
✓ Input validation with Pydantic
✓ Clean modular structure
✓ Clear separation of concerns
✓ Production-ready code

TESTING THE SYSTEM
════════════════════════════════════════════════════════════════

Health Check:
  $ curl http://localhost:8000/api/v1/health

Example Analysis:
  $ curl -X POST http://localhost:8000/api/v1/analyze \
      -H "Content-Type: application/json" \
      -d '{
        "text": "Chocolate bar with gelatin and nuts"
      }'

Interactive Testing:
  1. Open browser: http://localhost:8000/docs
  2. Click on POST /api/v1/analyze
  3. Click "Try it out"
  4. Enter test data
  5. Execute

TROUBLESHOOTING
════════════════════════════════════════════════════════════════

1. Missing GEMINI_API_KEY
   → Add your key to .env file

2. Module import errors
   → Run: pip install -r requirements.txt

3. Port already in use
   → Use different port: --port 8001

4. Slow API responses
   → Check network for search results
   → Gemini API calls take ~2-5 seconds

NEXT STEPS
════════════════════════════════════════════════════════════════

1. ✓ Get your GEMINI_API_KEY
2. ✓ Create .env with API key
3. ✓ Run: pip install -r requirements.txt
4. ✓ Start: python -m uvicorn app.main:app --reload
5. ✓ Visit: http://localhost:8000/docs
6. ✓ Test the API
7. ✓ Deploy to production

SUPPORT RESOURCES
════════════════════════════════════════════════════════════════

Documentation:
  • AGENTS.md  - Architecture specification
  • README.md  - API documentation
  • SETUP.md   - Production setup

Code:
  • app/main.py               - App entry point
  • app/services/orchestrator.py - Main logic
  • app/api/halal_check.py    - API routes

External Resources:
  • FastAPI Docs: https://fastapi.tiangolo.com/
  • Gemini API: https://ai.google.dev/
  • Pydantic: https://docs.pydantic.dev/

════════════════════════════════════════════════════════════════

✅ BUILD STATUS: COMPLETE & PRODUCTION READY
 Build Date: April 24, 2026
 Ready to Deploy

════════════════════════════════════════════════════════════════

EOF
