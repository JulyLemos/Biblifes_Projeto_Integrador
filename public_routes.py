from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from util import ler_html


router = APIRouter()
app = FastAPI()

templates = Jinja2Templates(directory = "templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@router.get("/")
def get_root(request: Request):
    html = ler_html("index")
    return HTMLResponse(html)

@router.get("/cadastro_livros")
def get_cadastro_livros(request: Request):
    html = ler_html("cadastro_livros")
    return HTMLResponse(html)
