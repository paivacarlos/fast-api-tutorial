from app.database.connection import connect_to_postgres
from app.database.register.getRegisterByIdQuery import get_register_by_id_query


async def get_register(register_id):
    conn = await connect_to_postgres()
    try:
        register_from_db = await get_register_by_id_query(conn, register_id)
        if register_from_db is not None:
            return dict(register_from_db)
        else:
            return None
    finally:
        await conn.close()
