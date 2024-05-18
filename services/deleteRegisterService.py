import re
import json
from database.connection import connect_to_postgres
from database.register.getRegisterByIdQuery import get_register_by_id_query
from database.register.deleteRegisterQuery import delete_register_query


async def delete_register_by_id(register_id):
    conn = await connect_to_postgres()
    try:
        # Verificar se o registro existe
        existing_register = await get_register_by_id_query(conn, register_id)
        if existing_register is None:
            return {"success": False, "message": "Register not found"}

        # Deletar o registro
        await delete_register_query(conn, register_id)
        return {"success": True, "message": "Register deleted with success"}
    finally:
        await conn.close()
