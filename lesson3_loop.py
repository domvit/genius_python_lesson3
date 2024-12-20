### Цикли:
#
# 1. **Таблиця множення:**
#    Завдання: Виведіть таблицю множення для заданого числа від 1 до 10.
#
# 2. **Сума чисел:**
#    Завдання: Визначте список чисел і обчисліть їх суму.
#
# 3. **Факторіал числа:**
#    Завдання: Обчисліть факторіал заданого числа.
#
# 4. **Парні числа:**
#    Завдання: Виведіть всі парні числа від 1 до 50.
#
# 5. **Пошук простих чисел:**
#    Завдання: Знайдіть всі прості числа в заданому діапазоні.
#
# Створіть власні змінні або встановіть початкові значення, щоб виконати ці завдання без використання `input`. Використовуйте умовні конструкції і цикли для розв'язання кожного завдання. Бажаю успіхів у виконанні цих завдань!
import math

# 1. **Таблиця множення:**
print('1. **Таблиця множення:**')
input_number = 7
number = 1
while number <= 10:
    print(input_number, 'x', number, '=', input_number * number)
    number += 1

# 2. **Сума чисел:**
print('2. **Сума чисел:**')
list_numbers = [1, 2, 3, 4, 5, 34, 355, 4]
summ = 0
for number in list_numbers:
    summ += number
print(summ)

# 3. **Факторіал числа:**
print('3. **Факторіал числа:**')
input_number = 4
number = 1
factorial = 1
while number <= input_number:
    factorial *= number
    number += 1
print('факторіал числа ', input_number, '', factorial)

# 4. **Парні числа:**
print('4. **Парні числа:**')
for number in range(1, 50):
    if number % 2 == 0:
        print(number)
        number += 1

# 5. **Пошук простих чисел:**
# Алгоритм перевірки на "просте число":
# Перевіряємо, чи число більше 1. (пропускаємо))
# Перевіряємо, чи воно ділиться без залишку на будь-яке число від 2 до квадратного кореня цього числа (включно).
# Якщо немає дільників — число просте.
print('5. **Пошук простих чисел:**')
begin_range = 17
end_range = 117

for number in range(begin_range, end_range):
    is_prime_number = True  # початково вважаємо число простим
    if number <= 1:
        is_prime_number = False  # Простих чисел менше або дорівнює 1 не існує
    else:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0: # Якщо знайшли дільник, то число не просте
                is_prime_number = False
                break
    if is_prime_number:
        print('Число', number, '- просте число')




