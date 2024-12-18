import uvicorn
from fastapi import FastAPI
from src.api.v1.user_routes import router as user_router

app = FastAPI()
app.include_router(user_router, prefix="/users", tags=["Users"])

# if __name__ == "__main__":
#     uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)