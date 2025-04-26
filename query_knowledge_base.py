import rdflib
from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS

# Crear un grafo RDF
g = Graph()

# Donde está el motor de inferencia?

# Definir los namespaces que usamos (opcional pero útil)
KINSHIP = Namespace("http://example.org/kinship#")
DATA = Namespace("http://example.org/data#")
# SCHEMA ya está predefinido en rdflib.namespace

# Cargar la ontología y los datos desde los archivos locales
# Asegúrate de que estos archivos estén en el mismo directorio que el script
# o proporciona la ruta completa.
try:
    g.parse("kinship.owl")
    # g.parse("kinship.ttl", format="turtle")
    print("Archivo kinship.ttl cargado correctamente.")
    g.parse("data.ttl", format="turtle")
    print("Archivo data.ttl cargado correctamente.")
except FileNotFoundError as e:
    print(f"Error: No se pudo encontrar el archivo {e.filename}. Asegúrate de que esté en la ruta correcta.")
    exit()
except Exception as e:
    print(f"Error al parsear los archivos TTL: {e}")
    exit()

print(f"Total de tripletas cargadas en el grafo: {len(g)}")

# --- Ejemplo de Consulta SPARQL ---
# Consulta para encontrar todas las instancias de :Person y sus nombres (schema:name)

query_all_persons = """
    PREFIX schema: <http://schema.org/>
    PREFIX kinship: <http://example.org/kinship#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT ?person ?name
    WHERE {
        ?person rdf:type kinship:Person .
        ?person schema:name ?name .
    }
"""

print("\n--- Personas en la Base de Conocimiento ---")
results = g.query(query_all_persons)

if not results:
    print("No se encontraron personas en el grafo.")
else:
    for row in results:
        # row[0] es la URI de la persona, row[1] es el Literal del nombre
        print(f"URI: {row.person}, Nombre: {row.name}")

# --- Otro Ejemplo: Encontrar los padres de Ana ---
query_ana_parents = """
    PREFIX schema: <http://schema.org/>
    PREFIX data: <http://example.org/data#>

    SELECT ?parent ?parentName
    WHERE {
        data:ana schema:parent ?parent .
        ?parent schema:name ?parentName .
    }
"""

print("\n--- Padres de Ana ---")
results_parents = g.query(query_ana_parents)

if not results_parents:
    print("No se encontraron padres para Ana.")
else:
    for row in results_parents:
        print(f"URI Padre/Madre: {row.parent}, Nombre: {row.parentName}")

# Haz un query para encontrar los hermanos de Maria.
query_ana_siblings = """
    PREFIX schema: <http://schema.org/>
    PREFIX data: <http://example.org/data#>

    SELECT ?sibling ?siblingName
    WHERE {
        ?sibling schema:parent ?parent.
        ?parent schema:name ?parentName.
        ?sibling schema:name ?siblingName.
       FILTER (?sibling != data:ana).
    }
"""
    #    FILTER (?parentName = "Maria").

print("\n--- Hermanos de Ana ---")
results_siblings = g.query(query_ana_siblings)

if not results_siblings:
    print("No se encontraron hermanos para Ana.")
else:
    # print(results_siblings)
    for row in results_siblings:
        print(f"URI Hermano: {row.sibling}, Nombre: {row.siblingName}")