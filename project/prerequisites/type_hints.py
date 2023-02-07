def total_price(price_1: int, price_2: int) -> str:
    return f'Your total bills is USD {price_1 + price_2}'


print(total_price(28,89))
print(total_price('28', '89'))

'''
First chapter about type hints, Mypy is a static type checker for Python!

To proceed with static type checking, follow the below steps:
1. Install mypy in your virtualenv, with pip install mypy==0.941
2.  Go to your python file path in the terminal and type: mypy filename.py

(venv) PS C:\lab\tutorial-fast-api\project\prerequisites> mypy .\type_hints.py
type_hints.py:4: error: Argument 1 to "total_price" has incompatible type "str"; expected "int"
type_hints.py:4: error: Argument 2 to "total_price" has incompatible type "str"; expected "int"
Found 2 errors in 1 file (checked 1 source file)

'''