from fastapi import FastAPI, HTTPException, status, Response
from model import Minha_playlist
from typing import Optional, List
# import requests

app = FastAPI(title="Músicas da minha Playlist", version="0.0.1", description="Uma lista com algumas músicas da minha playlist")

musicas = {
    1: {
        "nome": "Je Te Laisserai Des Mots",
        "banda": "Patrick Watson",
        "album": "Je Te Laisserai Des Mots",
        "genero": "Indie",
        "duracao": 2.42,
        "ano_lancamento": 2010
    },
    2: {
        "nome": "Tardes Que Nunca Acabam",
        "banda": "Baco Exu do Blues",
        "album": "Tardes que Nunca Acabam",
        "genero": "Rap",
        "duracao": 2.19,
        "ano_lancamento": 2018
    },
    3: {
        "nome": "Nobody",
        "banda": "Skindred",
        "album": "Babylon",
        "genero": "Reggae",
        "duracao": 3.23,
        "ano_lancamento": 2002
    },
    4: {
        "nome": "Once More to See You",
        "banda": "Mitski",
        "album": "Puberty 2",
        "genero": "Indie",
        "duracao": 3.01,
        "ano_lancamento": 2016
    },
    5: {
        "nome": "Tempo de Pipa",
        "banda": "Cícero Lins",
        "album": "Canções de Apartamento",
        "genero": "Indie",
        "duracao": 4.16,
        "ano_lancamento": 2011
    },
    6: {
        "nome": "Helipa",
        "banda": "Yago Oproprio",
        "album": "Helipa",
        "genero": "Rap",
        "duracao": 3.45,
        "ano_lancamento": 2022
    },
    7: {
        "nome": "Toda Beleza",
        "banda": "Rubel, Bala Desejo",
        "album": "As Palavras, Vol. 1 & 2",
        "genero": "MPB,  Samba",
        "duracao": 3.26,
        "ano_lancamento": 2023
    },
    8: {
        "nome": "B.Y.O.B",
        "banda": "System of Down",
        "album": "Mezmerize",
        "genero": "Thrash Metal",
        "duracao": 4.16,
        "ano_lancamento": 2005
    },
    9: {
        "nome": "Intro",
        "banda": "Pumapjl",
        "album": "Pumapjl & Febre90S",
        "genero": "Hip-Hop/Rap",
        "duracao": 1.15,
        "ano_lancamento": 2022
    },
    10: {
        "nome": "Like A Stone",
        "banda": "Audioslave",
        "album": "Audioslave",
        "genero": "Rock Alternativo",
        "duracao": 4.54,
        "ano_lancamento": 2002
    },
    11: {
        "nome": "Tanto Faz",
        "banda": "Urias",
        "album": "FÚRIA",
        "genero": "Pop",
        "duracao": 2.57,
        "ano_lancamento": 2022
    },
    12: {
        "nome": "Espero Que Entendam",
        "banda": "Ebony, LARINHAX",
        "album": "Espero Que Entendam",
        "genero": "Rap",
        "duracao": 3.19,
        "ano_lancamento": 2023
    },
    13: {
        "nome": "Caminhos",
        "banda": "BK'",
        "album": "Castelos & Ruínas",
        "genero": "Hip-Hop/Rap",
        "duracao": 3.10,
        "ano_lancamento": 2016
    }
}

#PEGANDO TODAS AS MUSICAS
@app.get("/musicas", summary="Retorna todas as musicas")
async def get_musicas():
    return musicas

#PEGANDO APENAS UMA MUSICA
@app.get("/musicas/{musica_id}")
async def get_musicas_ind(musica_id: int):
    try:
        musica = musicas[musica_id]
        return musica
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Musica não encontrada")
   
#CRIANDO UMA MUSICA NA API
@app.post("/musicas", status_code=status.HTTP_201_CREATED, description="Cria uma musica nova na playlist")
async def post_musica(musica: Optional[Minha_playlist] = None):
    try:
        next_id = len(musicas) + 1
        musicas[next_id] = musica
        del musica.id
        return musica
    except KeyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Já existe uma música com o ID {musica.id}")

#ATUALIZANDO UMA MUSICA NA API
@app.put("/musicas/{musica_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_musicas(musica_id: int, musica: Minha_playlist):
    if musica_id in musicas:
        musicas[musica_id] = musica
        musica.id = musica_id
        del musica.id
        return musica
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Música não encontrada")

#DELETANDO UMA MUSICA
@app.delete("/musicas/{musica_id}")
async def delete_musicas(musica_id: int):
    if musica_id in musicas:
        del musicas[musica_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Musica não encontrada")
        


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)