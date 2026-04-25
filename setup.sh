#!/bin/bash

echo "🧠 Halal Analyzer - Production Setup"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Create .env file from .env.example and add your GEMINI_API_KEY"
echo "2. Run: python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
echo ""
echo "🌐 API Documentation: http://localhost:8000/docs"

