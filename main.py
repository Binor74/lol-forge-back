from fastapi import FastAPI
from champions.champions_controller import router as champions_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include champions router
app.include_router(champions_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}