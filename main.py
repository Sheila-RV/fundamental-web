from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Esto permite que el frontend se conecte
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/saludo")
def saludo(nombre: str):
    return {"mensaje": f"Hola {nombre}, bienvenida a Bolivia 🇧🇴"}

@app.get("/call_to_action")
def call(edad:int):
    return {"call": f"Este año tienes {edad} años, haz que valgan la pena",
            "fin": f"El siguiente año tendrás {edad+1}, cuan intensamente viviste?"}
