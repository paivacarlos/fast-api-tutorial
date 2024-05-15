import re
import asyncpg
from dotenv import load_dotenv
import os
import json


load_dotenv()
database_url = os.getenv("DATABASE_URL")


async def connect_to_postgres():
    return await asyncpg.connect(f"{database_url}")


async def get_register(id_of_register):
    conn = await connect_to_postgres()
    try:
        register_from_db = await conn.fetchrow("SELECT * FROM register WHERE id = $1", id_of_register)
        register = register_from_db
        print(register)
        if register is not None:
            return dict(register)
        else:
            register = None
            return register
    finally:
        await conn.close()
