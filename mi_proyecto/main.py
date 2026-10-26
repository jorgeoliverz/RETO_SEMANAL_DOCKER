import os
import psycopg
from personajes import personajes

url = os.getenv("DATABASE_URL")

try:
    with psycopg.connect(url) as connection:
        with connection.cursor() as cur:
            cur.execute("INSERT INTO characters (id, name, status, species, type, gender, origin_name, location_name, image, url, created) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (1001, 'Pepe Taronja', 'Alive', 'Human', '', 'Male', 'Valencia', 'EDEM', NULL, NULL, '2026-10-26T10:00:00+01:00'),
    (1002, 'Lucía Fallera', 'Alive', 'Human', '', 'Female', 'Valencia', 'Ruzafa', NULL, NULL, '2026-10-26T10:00:00+01:00'),
    (1003, 'Toni Paella', 'Dead', 'Human', '', 'Male', 'Albal', 'La Albufera', NULL, NULL, '2026-10-26T10:00:00+01:00'),
    (1004, 'Marta Horchata', 'Alive', 'Human', '', 'Female', 'Alboraya', 'EDEM', NULL, NULL, '2026-10-26T10:00:00+01:00'),
    (1005, 'Zorg', 'Alive', 'Alien', 'Marciano', 'Male', 'Marte', 'EDEM', NULL, NULL, '2026-10-26T10:00:00+01:00'),
    (1006, 'Xilia', 'Alive', 'Alien', 'Venusiana', 'Female', 'Venus', 'Ciudad de las Artes', NULL, NULL, '2026-10-26T10:00:00+01:00'),
    (1007, 'Blurp', 'unknown', 'Alien', 'Gelatinoso', 'unknown', 'Plutón', 'Malvarrosa', NULL, NULL, '2026-10-26T10:00:00+01:00'),
    (1008, 'R2-Taronja', 'Alive', 'Robot', 'Asistente', 'unknown', 'Fábrica Ford', 'EDEM', NULL, NULL, '2026-10-26T10:00:00+01:00'),
    (1009, 'Docker-Bot', 'Alive', 'Robot', 'Contenedor', 'unknown', 'Servidor', 'Puerto 5432', NULL, NULL, '2026-10-26T10:00:00+01:00'),
    (1010, 'Unit-404', 'Dead', 'Robot', 'Antiguo', 'unknown', 'Desconocido', 'Chatarrería', NULL, NULL, '2026-10-26T10:00:00+01:00')
            )
            cur.execute("SELECT id, name, species FROM characters ORDER BY id LIMIT 10;")
            filas = cur.fetchall()
            
            for fila in filas:
                print(fila)
            
            cur.execute("SELECT COUNT(*) FROM characters;")
            total = cur.fetchone()[0]
            print(total)
except Exception as e:
    print("Error:", e)
    raise