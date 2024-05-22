import asyncpg
from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.getenv("DATABASE_URL")


async def connect_to_postgres():
    return await asyncpg.connect(f"{database_url}")
