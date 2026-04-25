# 🧠 🚀 **CORRECT ARCHITECTURE: HALAL AI ANALYZER SYSTEM**

## 🎯 Goal

Build a system that:

* Understands product text/images
* Extracts ingredients
* Uses **Gemini 3 Flash Preview**
* Uses **free web search for evidence**
* Combines AI + real-world data
* Returns **structured Uzbek response**

---

# 🏗️ 1. HIGH-LEVEL ARCHITECTURE

```text id="arch1"
                ┌──────────────────────────┐
                │       FastAPI API        │
                └────────────┬─────────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
     ┌────────────┐  ┌──────────────┐  ┌──────────────┐
     │ Classifier │  │ Ingredient AI│  │  Search API   │
     │ (Gemini)   │  │ (Gemini 3)   │  │ (Free Search) │
     └─────┬──────┘  └──────┬───────┘  └──────┬───────┘
           │                │                 │
           └────────────┬───┴───────┬────────┘
                        ▼           ▼
              ┌──────────────────────────┐
              │   Orchestrator Layer     │
              │ (Decision Engine)        │
              └────────────┬─────────────┘
                           ▼
              ┌──────────────────────────┐
              │  Final JSON Response     │
              │  (Uzbek output)          │
              └──────────────────────────┘
```

---

# ⚙️ 2. TECH STACK (FINAL)

## Backend

* FastAPI (async)
* Pydantic v2
* Uvicorn

## AI Engine

* 🧠 `gemini-3-flash-preview`

## Search Layer (FREE)

* DuckDuckGo scraping OR custom Google HTML parsing

## Database

* PostgreSQL (optional but recommended)
* SQLAlchemy async

---

# 🧠 3. CORE SERVICES DESIGN

---

## 🔵 3.1 Gemini Service (AI Brain)

### Responsibilities:

* classify product
* extract ingredients
* analyze halal status
* explain reasoning (Uzbek)

```python id="svc1"
class GeminiService:
    def classify_product(self, text): ...
    def extract_ingredients(self, text): ...
    def analyze_ingredient(self, ingredient): ...
```

---

## 🌐 3.2 Free Search Service (Evidence Layer)

### Responsibilities:

* search halal/haram discussions
* return links + snippets

```python id="svc2"
class FreeSearchService:
    def search(self, query: str):
        return [
            {
                "title": "...",
                "snippet": "...",
                "link": "..."
            }
        ]
```

✔ NO paid APIs
✔ DuckDuckGo / scraping

---

## ⚙️ 3.3 Orchestrator (MOST IMPORTANT)

This is your **AI brain controller**

### Flow:

```text id="flow1"
Input
 ↓
Product Classification
 ↓
IF not food → return early
 ↓
Extract ingredients
 ↓
FOR each ingredient:
    ├── Gemini analysis
    ├── Free search evidence
    └── merge result
 ↓
Final decision engine
 ↓
Return Uzbek JSON
```

---

# 🧠 4. GEMINI MODEL USAGE (IMPORTANT)

You MUST use:

```python id="model"
gemini-3-flash-preview
```

Usage pattern:

```python id="call"
self.model.generate_content(prompt)
```

---

# 🔥 5. FINAL DATA FLOW (REAL SYSTEM)

## Step-by-step:

### 1️⃣ Input

```json
{
  "text": "chocolate with gelatin"
}
```

---

### 2️⃣ Classification (Gemini)

```json
{
  "category": "food",
  "is_edible": true
}
```

---

### 3️⃣ Ingredients

```json
["chocolate", "gelatin"]
```

---

### 4️⃣ For each ingredient:

#### Gemini:

* halal reasoning

#### Search:

* real-world evidence

---

### 5️⃣ Merge Engine:

```text id="merge"
IF any false → false
IF any doubtful → doubtful
ELSE → true
```

---

### 6️⃣ Output (Uzbek JSON)

```json id="final"
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
  "overall_summary": "mahsulotda jelatin mavjudligi sababli shubhali"
}
```

---

# 🧱 6. PROJECT STRUCTURE (CORRECT)

```text id="structure"
app/
│
├── main.py
│
├── api/
│   └── halal_check.py
│
├── services/
│   ├── gemini_service.py
│   ├── search_service.py
│   └── orchestrator.py   ← MAIN LOGIC
│
├── models/
│   └── db_models.py
│
├── schemas/
│   └── halal_schema.py
│
├── core/
│   └── config.py
```

---

# ⚡ 7. WHY YOUR PREVIOUS VERSION FAILED

Because it was:

| Problem          | Reason                 |
| ---------------- | ---------------------- |
| No Gemini        | AI layer missing       |
| No search        | evidence layer missing |
| Rule-based logic | fake intelligence      |
| No orchestrator  | no system control      |

---

# 🚀 8. WHAT YOU NOW HAVE (NEW SYSTEM)

You are building:

> 🧠 **Hybrid AI Decision Engine**

It combines:

* LLM reasoning (Gemini)
* Real-world evidence (search)
* Deterministic logic (rules)
* Structured backend (FastAPI)

---

# 🔥 FINAL RESULT

Your system is now:

### ✔ Production-grade AI backend

### ✔ Scalable microservice-ready

### ✔ Cost-efficient (free search)

### ✔ Multilingual (Uzbek output)

### ✔ Explainable AI (reason + evidence)

