from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn
from icecream import ic
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        ic("lifespan startup")
        yield
    finally:
        await app.state.shutdown()



from routes.routes_auth import auth_router
from routes.routes_stripe import stripe_router
from routes.routes_websockets import websocket_router
from routes.routes_basic import basic_router
from routes.routes_play import play_router

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(stripe_router, prefix="/stripe", tags=["stripe"])
app.include_router(websocket_router, prefix="/websocket", tags=["websocket"])
app.include_router(basic_router, prefix="/basic", tags=["basic"])
app.include_router(play_router, prefix="/play", tags=["play"])



# Get the absolute path to the my_web_app directory
web_app_dir = os.path.join(os.path.dirname(__file__), "my_web_app")

# Mount the static directory
app.mount("/static", StaticFiles(directory=os.path.join(web_app_dir, "static")), name="static")

# Configure Jinja2 templates with explicit path
templates_dir = os.path.join(web_app_dir, "templates")
templates = Jinja2Templates(directory=templates_dir)
print(f"Templates directory: {templates_dir}")  # Debug output





@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/home")
async def home():
    return {"message": "Welcome to the home page"}


@app.get("/base", response_class=HTMLResponse)
async def read_base(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def read_login(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
