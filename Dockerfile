# ==============================================================================
# DOCKERFILE: PALADIN AGENT ENGINE (GEMINI ENTERPRISE AGENT PLATFORM)
# ==============================================================================
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080 \
    GOOGLE_GENAI_USE_VERTEXAI=true \
    GOOGLE_CLOUD_PROJECT=arsanjani-genai \
    GOOGLE_CLOUD_LOCATION=us-central1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy and install python dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY backend/ /app/backend/
COPY frontend/ /app/frontend/
COPY deploy/ /app/deploy/
COPY GEMINI.md architecture.md orchestration.md /app/

EXPOSE 8080

CMD ["python", "backend/app.py"]
