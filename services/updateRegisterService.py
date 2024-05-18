import re
import json
from database.connection import connect_to_postgres
from database.register.updateRegisterQuery import update_register_query


async def update_register(register_id, new_register_data):
    conn = await connect_to_postgres()
    try:
        await update_register_query(conn, register_id, new_register_data)
        return {"message": "Register updated successfully"}
    finally:
        await conn.close()
