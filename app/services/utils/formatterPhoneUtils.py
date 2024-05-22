import re


async def formatter_Phone(phone):
    phone_formatted = re.sub(r'\D', '', phone)
    return phone_formatted
