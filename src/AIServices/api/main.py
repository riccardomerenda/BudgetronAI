"""
BudgetronAI AI Services - Main FastAPI Application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from api.routers import categories, advisor, spending

# Create FastAPI app
app = FastAPI(
    title="BudgetronAI AI Services",
    description="AI-powered financial management services for BudgetronAI",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development - restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(categories.router, prefix="/api/categories", tags=["Categories"])
app.include_router(advisor.router, prefix="/api/advisor", tags=["Financial Advisor"])
app.include_router(spending.router, prefix="/api/spending", tags=["Spending Analysis"])


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint to verify the service is running."""
    return {
        "status": "operational",
        "service": "BudgetronAI AI Services",
        "version": "0.1.0"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)