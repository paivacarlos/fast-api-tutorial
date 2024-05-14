import re
import asyncpg
from dotenv import load_dotenv
import os


load_dotenv()
database_url = os.getenv("DATABASE_URL")


async def connect_to_postgres():
    return await asyncpg.connect(f"{database_url}")


async def get_registers():
    conn = await connect_to_postgres()
    try:
        registers = await conn.fetch("SELECT * FROM REGISTER")
    finally:
        await conn.close()
    return registers
