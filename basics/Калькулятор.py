def calculator():
    print("Простой калькулятор")
    num1 = float(input("Введите первое число: "))
    operator = input("Выберите операцию (+, -, *, /): ")
    num2 = float(input("Введите второе число: "))
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Ошибка: деление на ноль!"
    else:
        return "Неверная операция"
    
    return f"Результат: {result}"

print(calculator())