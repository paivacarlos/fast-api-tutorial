import re
from database.connection import connect_to_postgres
from database.register.createRegisterQuery import create_register_query
from .utils.formatterPhoneUtils import formatter_Phone


async def create_register(new_register):
    new_register.phone = await formatter_Phone(new_register.phone)
    # Conexão ao banco de dados PostgreSQL
    conn = await connect_to_postgres()

    try:
        # Executa a consulta SQL para inserir os dados na tabela
        new_register_id = await create_register_query(conn, new_register)
    finally:
        # Fecha a conexão com o banco de dados
        await conn.close()

    return {"message": "Register created with success!",
            "id": new_register_id}
