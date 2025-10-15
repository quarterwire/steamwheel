# main.py

from app.db.db import jsonData
from fastapi import FastAPI
from contextlib import asynccontextmanager  # 👈 New Import
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.services.cache import download_file
from app.controllers import game as game_controller

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

app.include_router(game_controller.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
