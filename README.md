# Basic Knowledge Graph Example: Kinship Ontology

This project demonstrates a simple knowledge graph representing kinship (family relationships) using RDF, OWL, and SPARQL. It utilizes the `rdflib` Python library to load ontology and data files, and execute queries.

## Project Structure

*   **`kinship.ttl`**: Defines the simple kinship ontology using the Turtle (TTL) syntax. It defines the `Person` class and properties like `hasMother`, `hasFather`, leveraging `schema.org` vocabulary.
*   **`kinship.owl`**: The same kinship ontology defined using the OWL/XML syntax.
*   **`data.ttl`**: Contains sample instance data (individuals representing family members) conforming to the kinship ontology, also in Turtle format.
*   **`query_knowledge_base.py`**: A Python script that loads the ontology (`kinship.owl` by default) and data (`data.ttl`) into an RDF graph using `rdflib`. It then executes sample SPARQL queries against the graph (e.g., finding all people, finding parents of a specific person).
*   **`requirements.txt`**: Lists the necessary Python package (`rdflib`).
*   **`.gitignore`**: Standard Python gitignore file.
*   **`README.md`**: This file.

## Setup

1.  **Clone the repository (if applicable):**
    ```bash
    git clone https://github.com/rafabelalcazar/knowledge_base_graph.git
    cd knowledge_base_graph
    ```

2.  **Create and activate a virtual environment:**
    *   On Windows:
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Queries

Ensure your virtual environment is activated. Then, run the Python script:

```bash
python query_knowledge_base.py