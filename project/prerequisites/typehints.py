def total_price(price_1: int, price_2: int) -> str:
    return f'Your total bills is USD {price_1 + price_2}'
print(total_price(28,89))
print(total_price('28', '89'))

'''
(venv) PS C:\lab\tutorial-fast-api\project\prerequisites> mypy .\typehints.py
typehints.py:4: error: Argument 1 to "total_price" has incompatible type "str"; expected "int"
typehints.py:4: error: Argument 2 to "total_price" has incompatible type "str"; expected "int"
Found 2 errors in 1 file (checked 1 source file)

'''