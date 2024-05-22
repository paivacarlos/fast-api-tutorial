from ..connection import connect_to_postgres


async def create_register_query(conn, new_register):
    row = await conn.fetchrow(
        "INSERT INTO register (name, cpf, address, phone) "
        "VALUES ($1, $2, $3, $4) RETURNING id",
        new_register.name,
        new_register.cpf,
        new_register.address,
        new_register.phone
    )
    return row['id']