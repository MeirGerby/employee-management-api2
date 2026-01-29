```mermaid


graph TD
    A[employee-management-api]

    A --> B[.github]
    B --> B1[workflows]
    B1 --> B2[ci.yml]

    A --> C[app]
    C --> C1[__init__.py]
    C --> C2[models.py]
    C --> C3[database.py]

    C --> D[routers]
    D --> D1[__init__.py]
    D --> D2[employees.py]
    D --> D3[missions.py]
    D --> D4[analysis.py]

    A --> E[tests]
    E --> E1[test_api.py]

    A --> F[main.py]
    A --> G[requirements.txt]
    A --> H[README.md]
    A --> I[.gitignore]
