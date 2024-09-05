from fastapi import FastAPI, Depends
import classes
import model
from database import engine, get_db
from sqlalchemy.orm import Session
from webscraping import scrape_ufu_categorias, save_to_db
from typing import List
from fastapi.   middleware.cors import CORSMiddleware

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "LALA"}

@app.get("/quadrado/{num}")
def square(num: int):
    return {"Quadrado": num ** 2}

@app.post("/criar")
def criar_valores(nova_mensagem: classes.Mensagem, db: Session = Depends(get_db)):
    mensagem_criada = model.Model_Mensagem(**nova_mensagem.model_dump())
    db.add(mensagem_criada)
    db.commit()
    db.refresh(mensagem_criada)
    return {"Mensagem": mensagem_criada}

@app.post("/scrape")
def scrape_and_save(db: Session = Depends(get_db)):
    categorias = scrape_ufu_categorias()
    save_to_db(categorias)
    return {"message": "Scraping concluído e dados inseridos no banco de dados."}

@app.get("/mensagens", response_model=List[classes.Mensagem], status_code=200)
async def buscar_valores(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    mensagens = db.query(model.Model_Mensagem).offset(skip).limit(limit).all()
    return mensagens
