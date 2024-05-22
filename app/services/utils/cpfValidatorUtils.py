def validate_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove non-numeric characters
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calculate_digit(digits):
        sum_value = sum(int(digit) * (index + 2) for index, digit in enumerate(reversed(digits)))
        return 11 - sum_value % 11

    first_digit = calculate_digit(cpf[:9])
    first_digit = first_digit if first_digit < 10 else 0

    second_digit = calculate_digit(cpf[:10])
    second_digit = second_digit if second_digit < 10 else 0

    return cpf[-2:] == f"{first_digit}{second_digit}"
