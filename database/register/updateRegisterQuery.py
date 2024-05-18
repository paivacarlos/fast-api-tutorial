from ..connection import connect_to_postgres


async def update_register_query(conn, register_id, new_data):
    await conn.execute(
        "UPDATE register SET name = $1, cpf = $2, address = $3, phone = $4 WHERE id = $5",
        new_data.name,
        new_data.cpf,
        new_data.address,
        new_data.phone,
        register_id,
    )
