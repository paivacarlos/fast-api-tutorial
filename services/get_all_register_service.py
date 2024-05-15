import re
import asyncpg
from dotenv import load_dotenv
import os
import json


load_dotenv()
database_url = os.getenv("DATABASE_URL")


async def connect_to_postgres():
    return await asyncpg.connect(f"{database_url}")


async def get_registers():
    conn = await connect_to_postgres()
    try:
        registers_from_db = await conn.fetch("SELECT * FROM register")
        registers = [dict(register) for register in registers_from_db]
    finally:
        await conn.close()
    data = registers
    return data
