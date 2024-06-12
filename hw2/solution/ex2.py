def parse_input(user_input: str):
    tokens = user_input.split()
    if len(tokens) != 4:
        raise Exception("Incorrect syntax")

    operation = tokens[0]
    if not operation in ['add', 'subtract', 'multiply', 'divide']:
        raise Exception('Incorrect operation')

    numbers = [float(tokens[1]), float(tokens[-1])]
    if numbers[0] is None or numbers[1] is None:
        raise Exception('Incorrect numbers')

    return operation, numbers


def calculate(operation: str, numbers: list) -> float:
    if operation == 'add':
        return numbers[0] + numbers[1]
    elif operation == 'subtract':
        return numbers[0] - numbers[1]
    elif operation == 'multiply':
        return numbers[0] * numbers[1]
    elif operation == 'divide':
        if numbers[1] == 0:
            raise Exception("Cannot divide by zero.")
        return numbers[0] / numbers[1]


def main():
    user_input = input("Enter your operation: ")
    operation, numbers = parse_input(user_input)
    try:
        result = calculate(operation, numbers)
        print(f"The answer is {result}")
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()
