import re
import asyncpg
from dotenv import load_dotenv
import os
import json
from database.connection import connect_to_postgres


async def update_register(register_id, new_register_data):
    conn = await connect_to_postgres()
    try:
        await conn.execute(
            "UPDATE register SET name = $1, cpf = $2, address = $3, phone = $4 WHERE id = $5",
            new_register_data.name,
            new_register_data.cpf,
            new_register_data.address,
            new_register_data.phone,
            register_id,
        )
        return {"message": "Register updated successfully"}
    finally:
        await conn.close()
