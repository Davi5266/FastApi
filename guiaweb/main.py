from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def helloWorld():
    return {
        "message":"Hello World!",
        "message02":"Games",
        "message03":"Supermario",
        "message04":"mmx"
        }

@app.post("/games/{game:str}")
async def games(game):
    return {
        "message": game
    }

dictData = {
    1:{"game":"gta5", "stars":5,"difficulty":"3.5"},
    1:{"game":"gta4", "stars":8,"difficulty":5},
    2:{"game":"DBZ", "stars":9,"difficulty":8},
    3:{"game":"need for speed", "stars":10,"difficulty":9},
    4:{"game":"megaman x", "stars":10,"difficulty":10},
    5:{"game":"five nigths", "stars":5,"difficulty":7},
    6:{"game":"bleach brave souls", "stars":10,"difficulty":9},
    7:{"game":"Deadpoll", "stars":4,"difficulty":6 }
}

@app.get("/dict")
async def dictTeste():
    return {"message":dictData}

# Consultando elementos através do indice
@app.get("/gamestest/{id_game}")
async def gamesTeste(id_game:int):
    if id_game in dictData:
        return dictData[id_game]
    else:
        return {"Erro":"Jogo não encontrado"}

@app.get("/gametest/{game}")
async def games(game: str):
    return {
        "message": game
    }