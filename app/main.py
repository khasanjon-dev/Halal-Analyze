from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.halal_check import router
from app.core.config import settings

app = FastAPI(
    title="Halal Analyzer API",
    description="AI-powered Halal product analysis using Gemini 3 Flash Preview",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
async def root():
    return {
        "message": "Halal Analyzer API",
        "docs": "/docs",
        "health": "/api/v1/health",
        "analyze": "/api/v1/analyze"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )

