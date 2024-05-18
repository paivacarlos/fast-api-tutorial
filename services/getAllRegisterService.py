import re
import json
from database.connection import connect_to_postgres


async def get_registers():
    conn = await connect_to_postgres()
    try:
        registers_from_db = await conn.fetch("SELECT * FROM register")
        registers = [dict(register) for register in registers_from_db]
    finally:
        await conn.close()
    data = registers
    return data
