from typing import Optional
from pydantic import BaseModel

class Minha_playlist(BaseModel):
    id: Optional[int] = None
    nome: str
    banda: str
    album: str
    genero: str
    duracao: float
    ano_lancamento: int
    