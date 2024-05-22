from app.database.connection import connect_to_postgres
from app.database.register.updateRegisterQuery import update_register_query
from .utils.formatterPhoneUtils import formatter_Phone


async def update_register(register_id, new_register_data):
    new_register_data.phone = await formatter_Phone(new_register_data.phone)
    conn = await connect_to_postgres()
    try:
        await update_register_query(conn, register_id, new_register_data)
        return {"message": "Register updated successfully"}
    finally:
        await conn.close()
