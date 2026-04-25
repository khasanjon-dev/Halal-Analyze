# Halal Analyzer - Production API

AI-powered Halal product analysis system using Google Gemini 3 Flash Preview with real-time web search evidence.

## Architecture

```
FastAPI App
    ├── GeminiService (Classification + Ingredient Extraction + Analysis)
    ├── FreeSearchService (DuckDuckGo for evidence)
    └── Orchestrator (Decision Engine)
```

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create `.env` file:
```
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-3-flash-preview
DEBUG=False
HOST=0.0.0.0
PORT=8000
```

## Running

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API Documentation: `http://localhost:8000/docs`

## API Endpoints

### POST /api/v1/analyze
Analyze product for Halal compliance.

**Request:**
```json
{
  "text": "chocolate with gelatin"
}
```

**Response:**
```json
{
  "product_name": "Chocolate",
  "category": "food",
  "is_edible": true,
  "is_halal": "doubtful",
  "ingredients_analysis": [
    {
      "ingredient": "gelatin",
      "is_halal": "doubtful",
      "reason": "jelatin manbasi noma'lum",
      "confidence": 80,
      "evidence": [
        {
          "title": "...",
          "link": "..."
        }
      ]
    }
  ],
  "overall_summary": "Mahsulotda jelatin mavjudligi sababli shubhali",
  "google_evidence_used": true
}
```

### GET /api/v1/health
Health check.

## Project Structure

```
app/
├── main.py                    # FastAPI app
├── api/
│   └── halal_check.py        # Route handlers
├── services/
│   ├── gemini_service.py     # AI classification/analysis
│   ├── search_service.py     # Web search
│   └── orchestrator.py       # Main logic
├── schemas/
│   └── halal_schema.py       # Pydantic models
├── models/
│   └── db_models.py          # Database models
└── core/
    └── config.py             # Configuration
```

## Features

✅ Gemini 3 Flash Preview AI  
✅ Product classification & ingredient extraction  
✅ Halal status determination  
✅ Real-time web search evidence  
✅ Structured JSON output  
✅ Uzbek language support  
✅ Production-ready FastAPI  

## Merging Logic

- If ANY ingredient is `false` → product is `false` (HARAM)
- Else if ANY ingredient is `doubtful` → product is `doubtful`
- Else → product is `true` (HALAL)

