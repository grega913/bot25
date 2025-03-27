from typing import Union
from contextlib import asynccontextmanager
from pydantic import BaseModel
from fastapi import FastAPI, Request, WebSocket, Depends, APIRouter, HTTPException, Body, status, Response, Path
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from markupsafe import escape
import uvicorn
from icecream import ic
import os
import firebase_admin
from firebase_admin import credentials, firestore
from helperz import SessionData, verifier, cookie
from typing import Optional

