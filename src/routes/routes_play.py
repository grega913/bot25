from fastapi import APIRouter
from fastapi import FastAPI, Request, WebSocket, Depends, APIRouter, HTTPException, Body, status, Response, Path
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from icecream import ic
import os

routes_dir = os.path.join(os.path.dirname(__file__))
src_dir = os.path.dirname(routes_dir)
templatesDir =  os.path.join(src_dir, "my_web_app/templates")
templates = Jinja2Templates(directory=templatesDir)

play_router = APIRouter()



# playground route
@play_router.get("/play", response_class=HTMLResponse)
async def play(request: Request):
    return templates.TemplateResponse(request=request, name="play/play.html")


# playground route
@play_router.get("/bulma1", response_class=HTMLResponse)
async def bulma1(request: Request):
    return templates.TemplateResponse(request=request, name="play/bulma1.html")
