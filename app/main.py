from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from app.routers.matches import router as match_router
from app.routers.players import router as player_router

app = FastAPI()
app.include_router(match_router)
app.include_router(player_router)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://4.245.64.27",
    "http://4.245.64.27:3000",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
