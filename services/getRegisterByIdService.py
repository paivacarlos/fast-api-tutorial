import re
import json
from database.connection import connect_to_postgres


async def get_register(id_of_register):
    conn = await connect_to_postgres()
    try:
        register_from_db = await conn.fetchrow("SELECT * FROM register WHERE id = $1", id_of_register)
        register = register_from_db
        if register is not None:
            return dict(register)
        else:
            register = None
            return register
    finally:
        await conn.close()
