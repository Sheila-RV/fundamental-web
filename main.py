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

DATABASE_URL = "postgresql://fundamental_db_user:yYLqLccz1MYnIE0uKIC6ED9MCWzdkacl@dpg-d6htntp5pdvs73do4am0-a.oregon-postgres.render.com/fundamental_db"

def get_connection():
    return psycopg2.connect(DATABASE_URL)

# Crea la tabla si no existe
def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS nombres (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

init_db()

@app.get("/saludo")
def saludo(nombre: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO nombres (nombre) VALUES (%s)", (nombre,))
    conn.commit()
    cur.close()
    conn.close()
    return {"mensaje": f"Hola {nombre}, bienvenida a Bolivia 🇧🇴"}

@app.get("/nombres")
def get_nombres():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT nombre FROM nombres ORDER BY id DESC")
    nombres = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return {"nombres": nombres}

@app.get("/call_to_action")
def call(edad:int):
    return {"call": f"Este año tienes {edad} años, haz que valgan la pena",
            "fin": f"El siguiente año tendrás {edad+1}, cuan intensamente viviste?"}
