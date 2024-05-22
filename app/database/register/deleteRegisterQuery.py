from ..connection import connect_to_postgres


async def delete_register_query(conn, register_id):
    await conn.execute(
        "DELETE FROM register WHERE id = $1", register_id
    )