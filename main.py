from complex_number import ComplexNumber
from complex_operations import ComplexNumberAddition, ComplexNumberMultiplication, ComplexNumberDivision


def get_complex_input(prompt):
    while True:
        try:
            real = float(input(prompt + " (действительная часть): "))
            imaginary = float(input(prompt + " (мнимая часть): "))
            return ComplexNumber(real, imaginary)
        except ValueError:
            print("Пожалуйста, введите действительное число.")


def main():
    print("Добро пожаловать в калькулятор комплексных чисел!")

    a = get_complex_input("Введите первое комплексное число")
    b = get_complex_input("Введите второе комплексное число")

    print("\nВыберите операцию:")
    print("1. Сложение")
    print("2. Умножение")
    print("3. Деление")

    while True:
        choice = input("Введите ваш выбор (1/2/3): ")
        if choice in ["1", "2", "3"]:
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

    if choice == "1":
        operation = ComplexNumberAddition()
    elif choice == "2":
        operation = ComplexNumberMultiplication()
    elif choice == "3":
        operation = ComplexNumberDivision()

    result = operation.execute(a, b)
    print(f"Результат: {result}")


if __name__ == "__main__":
    main()
