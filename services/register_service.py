import re
import asyncpg
from dotenv import load_dotenv
import os


load_dotenv()
database_url = os.getenv("DATABASE_URL")


async def connect_to_postgres():
    return await asyncpg.connect(f"{database_url}")


async def create_register(new_register):
    new_register.phone = re.sub(r'\D', '', new_register.phone)
    # Conexão ao banco de dados PostgreSQL
    conn = await connect_to_postgres()

    try:
        # Executa a consulta SQL para inserir os dados na tabela
        await conn.execute("INSERT INTO register (name, cpf, address, phone) "
                           "VALUES ($1, $2, $3, $4)",
                           new_register.name,
                           new_register.cpf,
                           new_register.address,
                           new_register.phone)
    finally:
        # Fecha a conexão com o banco de dados
        await conn.close()

    return {"message": "Register created with success!"}
