from fastapi import FastAPI
from app.core.config import settings


# Create a FastAPI instance
app = FastAPI(
    title=settings.APP_NAME,
    description="API para cotação automatica",
    version="1.0.0",
)

@app.get("/health")
def health_check():
    return {"message": "API is running smoothly,", "status": "healthy", "environment": settings.ENVIRONMENT}
#Inclusão das rotas 
from routes.main import Main_router
app.include_router(prefix='/auth', router=Main_router)

