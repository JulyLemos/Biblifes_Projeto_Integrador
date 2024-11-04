from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from models.livro_model import Livro
from models.usuario_model import Usuario
import public_routes
from repositories import livro_repo, usuario_repo
from util import ler_html

usuario_repo.criar_tabela()
livro_repo.criar_tabela_livro()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")
# static = Jinja2Templates(directory="static")

app.include_router(public_routes.router)
# @app.get("/")
# def get_root(request: Request):
#     html = ler_html("index")
#     return HTMLResponse(html)
# @app.get("/cadastro_livros")
# def get_cadastro_livros(request: Request):
#     html = ler_html("cadastro_livros")
#     return HTMLResponse(html)

@app.post("/post_cadastro_livros")
def post_cadastro_livros(
    titulo: str = Form(...),
    autor: str = Form(...),
    ano: str = Form(...),
    paginas: str = Form(...),
    edicao: str = Form(...),
    idioma: str = Form(...),
    editora: str = Form(...),
    isbn: str = Form(...),
    genero1: str = Form(...),
    genero2: str = Form(...),
    sinopse: str = Form(...)):
    livro = Livro(None, titulo, autor, ano, paginas, edicao, idioma, editora, isbn, genero1, genero2, sinopse)
    livro = livro_repo.inserir_livro(livro)
    if livro:
        return RedirectResponse("/lar", 303)
    else:
        return RedirectResponse("/cadastro_livros", 303)

@app.get("/lar")
def get_lar(request: Request):
    html = ler_html("lar")
    return HTMLResponse(html)

@app.get("/login")
def get_login(request: Request):
    html = ler_html("login")
    return HTMLResponse(html)

@app.get("/cadastro")
def get_cadastro(request: Request):
    html = ler_html("cadastro")
    return HTMLResponse(html)

@app.post("/post_cadastro")
def post_cadastro(
    matricula: str = Form(...),
    cpf: str = Form(...)):
    usuario = Usuario(None, matricula, cpf) 
    usuario = usuario_repo.inserir(usuario)
    return RedirectResponse("/lar", 303)

@app.get("/cadastro_recebido")
def get_lar(request: Request):
    html = ler_html("cadastro_recebido")
    return HTMLResponse(html)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)