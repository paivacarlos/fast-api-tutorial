from ..connection import connect_to_postgres


async def create_register_query(conn, new_register):
    await conn.execute(
        "INSERT INTO register (name, cpf, address, phone) "
        "VALUES ($1, $2, $3, $4)",
        new_register.name,
        new_register.cpf,
        new_register.address,
        new_register.phone
    )