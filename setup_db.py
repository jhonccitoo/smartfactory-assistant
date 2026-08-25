import sqlite3

conn = sqlite3.connect("smartfactory.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE indicadores (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    valor REAL,
    fecha TEXT
)
""")

cur.execute("""
CREATE TABLE incidencias (
    id INTEGER PRIMARY KEY,
    descripcion TEXT,
    severidad TEXT,
    fecha TEXT
)
""")

cur.executemany("INSERT INTO indicadores VALUES (?,?,?,?)", [
    (1, "Produccion diaria (ton)", 452.3, "2026-06-18"),
    (2, "Eficiencia OEE (%)", 87.5, "2026-06-18"),
    (3, "Consumo energetico (kWh)", 12300, "2026-06-18"),
])

cur.executemany("INSERT INTO incidencias VALUES (?,?,?,?)", [
    (1, "Paro no programado en linea 2 por falla de sensor", "Alta", "2026-06-17"),
    (2, "Retraso en abastecimiento de materia prima", "Media", "2026-06-16"),
])

conn.commit()
conn.close()
print("Base de datos creada: smartfactory.db")