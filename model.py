from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.sql import text
from database import Base

class Model_Mensagem(Base):
    __tablename__ = "mensagens"

    id = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String, nullable=False)
    conteudo = Column(String, nullable=False)
    publicada = Column(Boolean, nullable=False)
    data_criacao = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)
    data_atualizacao = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)

class Model_Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, nullable=False)
    menuNav = Column(String, nullable=False)
    link = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)