import re
import asyncpg
from dotenv import load_dotenv
import os
import json
from database.connection import connect_to_postgres


async def delete_register_by_id(register_id):
    conn = await connect_to_postgres()
    try:
        # Verificar se o registro existe
        existing_register = await conn.fetchrow("SELECT * FROM register WHERE id = $1", register_id)
        if existing_register is None:
            return {"success": False, "message": "Register not found"}

        # Deletar o registro
        await conn.execute("DELETE FROM register WHERE id = $1", register_id)
        return {"success": True, "message": "Register deleted with success"}
    finally:
        await conn.close()
