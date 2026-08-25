import chromadb
from pypdf import PdfReader
import ollama
import os

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("documentos_smartfactory")

def chunk_text(text, size=500):
    return [text[i:i+size] for i in range(0, len(text), size)]

for archivo in os.listdir("documentos"):
    if archivo.endswith(".pdf"):
        reader = PdfReader(f"documentos/{archivo}")
        texto_completo = ""
        for page in reader.pages:
            texto_completo += page.extract_text()

        chunks = chunk_text(texto_completo)
        for i, chunk in enumerate(chunks):
            embedding = ollama.embeddings(model="nomic-embed-text", prompt=chunk)["embedding"]
            collection.add(
                ids=[f"{archivo}_{i}"],
                embeddings=[embedding],
                documents=[chunk],
                metadatas=[{"fuente": archivo}]
            )
        print(f"Indexado: {archivo} ({len(chunks)} fragmentos)")

print("Indexacion completa")