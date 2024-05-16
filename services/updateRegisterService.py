import re
import asyncpg
from dotenv import load_dotenv
import os
import json


load_dotenv()
database_url = os.getenv("DATABASE_URL")


async def connect_to_postgres():
    return await asyncpg.connect(f"{database_url}")


async def update_register(register_id, new_data):
    conn = await connect_to_postgres()
    try:
        await conn.execute(
            "UPDATE register SET name = $1, cpf = $2, address = $3, phone = $4 WHERE id = $5",
            new_data.name,
            new_data.cpf,
            new_data.address,
            new_data.phone,
            register_id,
        )
        return {"message": "Register updated successfully"}
    finally:
        await conn.close()
