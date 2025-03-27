from fastapi import FastAPI, Request, WebSocket, Depends, APIRouter, HTTPException, Body, status, Response, Path, WebSocketDisconnect
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from icecream import ic


routes_dir = os.path.join(os.path.dirname(__file__))
src_dir = os.path.dirname(routes_dir)
templatesDir =  os.path.join(src_dir, "my_web_app/templates")
templates = Jinja2Templates(directory=templatesDir)
websocket_router = APIRouter()


@websocket_router.get("/test_websocket", response_class=HTMLResponse)
async def test_websocket(request: Request):
    return templates.TemplateResponse(request=request, name="websockets/test_websocket.html")


@websocket_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # Process the data
            await websocket.send_text(f"Received: {data}")
    except WebSocketDisconnect:
        ic("WebSocket connection closed")  # Log the disconnection
        # Perform cleanup tasks here

