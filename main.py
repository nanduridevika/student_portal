from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html"
    )

@app.post("/login")
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "username": username,
            "password": password,
            "message": "Login form submitted successfully!"
        }
    )
