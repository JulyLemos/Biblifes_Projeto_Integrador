SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        matricula TEXT NOT NULL,
        cpf TEXT NOT NULL
    )
"""

SQL_INSERIR = """
    INSERT INTO usuario (
        matricula, cpf)
    VALUES (?, ?)
"""

SQL_OBTER_TODOS = """
    SELECT id, matricula, cpf
    FROM usuario
    ORDER BY matricula
"""