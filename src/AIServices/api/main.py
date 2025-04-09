from fastapi import FastAPI

app = FastAPI(
    title="BudgetronAI API",
    description="AI-powered financial management services",
    version="0.1.0"
)


@app.get("/health")
async def health_check():
    """Health check endpoint to verify the service is running."""
    return {"status": "operational", "message": "BudgetronAI AI Service Operational v2.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)