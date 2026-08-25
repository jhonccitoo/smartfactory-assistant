\# SmartFactory Assistant



Asistente con IA que permite consultar indicadores operativos, incidencias y documentación interna en lenguaje natural, combinando RAG sobre PDFs con consulta a base de datos estructurada.



\## Stack

\- Python + FastAPI

\- n8n (orquestación)

\- Ollama (LLM local — Llama 3.1 8B)

\- ChromaDB (búsqueda semántica)

\- SQLite (datos operativos)



\## Arquitectura

Usuario → n8n Webhook → FastAPI → SQLite + ChromaDB → LLM → Respuesta



\## Instalación



\### 1. Requisitos previos

\- Python 3.10+

\- Node.js 18+

\- \[Ollama](https://ollama.com/download) instalado



\### 2. Clonar el repositorio

```bash

git clone https://github.com/jhonccitoo/smartfactory-assistant.git

cd smartfactory-assistant

```



\### 3. Crear entorno virtual e instalar dependencias

```bash

python -m venv venv

venv\\Scripts\\Activate.ps1   # Windows

pip install -r requirements.txt

```



\### 4. Descargar modelos de Ollama

```bash

ollama pull llama3.1:8b

ollama pull nomic-embed-text

```



\### 5. Crear la base de datos

```bash

python setup\_db.py

```



\### 6. Indexar documentos PDF

```bash

python indexar.py

```



\### 7. Levantar la API

```bash

uvicorn api:app --reload --port 8000

```



\### 8. Levantar n8n

```bash

n8n

```

Abrir http://localhost:5678 e importar el workflow.



\### 9. Abrir el chat

Abrir `chat-smartfactory.html` en el navegador.



\## Consultas de ejemplo

\- ¿Cuál es la producción de hoy?

\- ¿Qué incidencias de severidad alta hay?

\- ¿Cuál es la política de mantenimiento de la línea 2?

\- ¿Qué se debe hacer ante un paro no programado?

