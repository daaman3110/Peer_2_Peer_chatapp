from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routes import router
from app.core.tasks import start_background_tasks


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await start_background_tasks()
    yield
    # Shutdown


app = FastAPI(lifespan=lifespan)
app.include_router(router)
