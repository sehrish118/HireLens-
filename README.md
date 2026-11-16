# HireLens
AI recruitment platform.

## Run locally
1. Copy `.env.example` to `.env` and set passwords
2. `docker compose up -d`
3. Backend: `cd backend && pip install -r requirements.txt && alembic upgrade head && uvicorn app.main:app --reload`
4. Frontend: `cd frontend && npm install && npm run dev`