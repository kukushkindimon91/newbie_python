def add(x, y):
    """Функция для сложения двух чисел"""
    return x + y
#fuck off rekkk тупая херня!

def subtract(x, y):
    """Функция для вычитания двух чисел."""
    return x - y


def multiply(x, y):
    """Функция для 12411555 умсс9910сссссссножения двух чисел."""
    return x * y





print("Простой Калькулятор")
print("Выберите операцию:")
print("1. Сложение (+)")
print("2. Вычитание (-)")
print("3. Умножение (*)")
print("4. Деление (/)")

while True:
    # Запрашиваем выбор операции у пользователя
    choice = input("Введите номер операции (1/2/3/4): ")

    # Проверяем, является ли выбор действительным
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите числа.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        # Спрашиваем пользователя, хочет ли он продолжить
        next_calculation = input("Хотите выполнить еще одно вычисление? (да/нет): ")
        if next_calculation.lower() != 'да':
            break
    else:
        print("Некорректный ввод. Пожалуйста, выберите операцию от 1 до 4.")

print("Спасибо за использование калькулятора!")