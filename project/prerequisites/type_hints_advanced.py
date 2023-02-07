from typing import Union

x: list[Union[int | float]] = [2, 3, 4.1, 5, 6.2]

print(x)


def inr_to_usd(value: float) -> Union[float, None]:
    try:
        conversion_factor = 75
        value = value/conversion_factor
        return value
    except TypeError:
        return None


print(inr_to_usd(89.44))
print(inr_to_usd('23'))


# Other way to create hints!
def smart_divide(func):
    def inner(a, b):
        if b == 0:
            print("Whoops! Division by 0")
            return None

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


divide(9, 0)

