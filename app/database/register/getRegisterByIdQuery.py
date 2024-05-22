from ..connection import connect_to_postgres


async def get_register_by_id_query(conn, register_id):
    print("Dentro do file query: ", register_id)
    result = await conn.fetchrow(
        "SELECT * FROM register WHERE id = $1", register_id
    )
    return result
