from fastapi import FastAPI, HTTPException # Core FastAPI functionality
from pydantic import BaseModel             # For data validation
from typing import Optional                # For optional fields
import logging                            # For application logging

# Setting up basic logging with INFO level
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__) # Created logger for this module

# Initializing FastAPI app with metadata
app = FastAPI(
    title="Healthcare LLM Optimizer",
    description="Medical domain-specific LLM inference API with adapter switching",
    version="1.0.0"
)

# Defining data models for request and response
class QueryInput(BaseModel):
    text: str
    adapter: Optional[str] = None
    max_tokens: Optional[int] = 512

class QueryResponse(BaseModel):
    text: str
    adapter_used: str
    processing_time: float #time taken for processing

# Health check endpoint
@app.get("/health")                      # GET endpoint at /health
async def health_check():
    """Endpoint to check if API is running"""
    return {
        "status": "healthy",
        "service": "Healthcare LLM Optimizer"
    }

# Main inference endpoint

@app.post("/generate", response_model=QueryResponse)  # POST endpoint at /generate
async def generate_text(query: QueryInput):
    """Generate medical text based on input query"""
    try:
        # Placeholder for LLM implementation
        return QueryResponse(
            text="Sample response (LLM implementation pending)",
            adapter_used="base",
            processing_time=0.0
        )
    except Exception as e:
        logger.error(f"Error during inference: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Error handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """
    Global error handler
    """
    return {"error": str(exc.detail), "status_code": exc.status_code}
#main entry point
if __name__ == "__main__":               # Run server if file is executed directly
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Start uvicorn servers