# main.py

from app.db.db import jsonData
from fastapi import FastAPI
from contextlib import asynccontextmanager  # 👈 New Import
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.services.cache import download_file
from app.controllers import game as game_controller
from fastapi.middleware.cors import CORSMiddleware

# CORS Policy
origins = ["http://localhost:5173", "http://localhost:5173"]


# Initialize the scheduler instance
scheduler = AsyncIOScheduler(id="ye")

# -------------------
# 1. Lifespan Context Manager
# -------------------


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles startup and shutdown events for the application.
    """

    print("--- Application Startup ---")

    trigger = IntervalTrigger(hours=10)
    scheduler.add_job(
        download_file,
        trigger,
        name="daily_cache",
    )
    scheduler.start()
    print("Scheduler started successfully.")
    jsonData
    yield

    print("--- Application Shutdown ---")
    if scheduler.running:
        scheduler.shutdown()
        print("Scheduler shut down.")


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(game_controller.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
