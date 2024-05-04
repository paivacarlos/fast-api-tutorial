def get_full_name(first_name: str, last_name: str):
    full_name = f"{first_name.title()} {last_name.title()}"
    return full_name


print(get_full_name("carlos", "paiva"))


def get_name_with_age(name: str, age: int):
    name_with_age = f"{name.title()} is this old {age}"
    return name_with_age


print(get_name_with_age("adolfo de mello", 35))


# we can use different types of data through arguments
def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e


# Using Union in the python 3.10+
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


say_hi("Paiva")
say_hi(None)
