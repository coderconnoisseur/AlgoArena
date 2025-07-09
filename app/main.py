from fastapi import FastAPI, Request,Depends
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routes import problem, user, contest
from fastapi.responses import HTMLResponse
from app.database import get_db
from app.models.problem import Problem as ProblemModel # Import the SQLAlchemy Problem model

app = FastAPI(title="AlgoArena", description="A competitive programming platform")

# Mount frontend files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configure templates
templates = Jinja2Templates(directory="app/templates")

app.include_router(problem.router)
app.include_router(user.router)
app.include_router(contest.router)

@app.get('/index')
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})


@app.get('/problems',response_class=HTMLResponse)
async def problems(request:Request,db:Session=Depends(get_db),page:int =1):
    page_size=100
    total=db.query(ProblemModel).count() 
    total_pages=(total+page_size-1)//page_size
    problems=db.query(ProblemModel).offset((page-1)*page_size).limit(page_size).all() 
    return templates.TemplateResponse(
        'problems.html',
        {'request':request,
        'problems':problems,
        'total_pages':total_pages,
        'current_page':page
        })

@app.get('/users')
async def users():
    return {"users": []}