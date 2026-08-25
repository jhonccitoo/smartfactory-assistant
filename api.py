from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3, chromadb, ollama

app = FastAPI()
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("documentos_smartfactory")

class Pregunta(BaseModel):
    consulta: str

@app.post("/preguntar")
def preguntar(p: Pregunta):
    # 1. Buscar contexto en documentos (RAG)
    emb = ollama.embeddings(model="nomic-embed-text", prompt=p.consulta)["embedding"]
    resultados = collection.query(query_embeddings=[emb], n_results=3)
    contexto_docs = "\n".join(resultados["documents"][0]) if resultados["documents"] else ""

    # 2. Buscar contexto en la base de datos
    conn = sqlite3.connect("smartfactory.db")
    cur = conn.cursor()
    cur.execute("SELECT nombre, valor, fecha FROM indicadores")
    indicadores = cur.fetchall()
    cur.execute("SELECT descripcion, severidad, fecha FROM incidencias")
    incidencias = cur.fetchall()
    conn.close()

    contexto_datos = f"Indicadores: {indicadores}\nIncidencias: {incidencias}"

    # 3. Generar respuesta con el LLM
    prompt = f"""Eres un asistente de SmartFactory SAC. Responde la consulta usando SOLO el contexto dado.

Contexto de documentos:
{contexto_docs}

Contexto de datos operativos:
{contexto_datos}

Consulta: {p.consulta}

Respuesta clara y concisa:"""

    respuesta = ollama.generate(model="llama3.1:8b", prompt=prompt)

    return {"respuesta": respuesta["response"]}