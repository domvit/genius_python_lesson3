### Умовні конструкції:
#
# 1. **Перевірка паролю:**
#    Завдання: Напишіть програму, яка встановлює початковий пароль і перевіряє, чи введений користувачем пароль співпадає з ним. Якщо пароль дорівнює "password123", виведіть повідомлення "Ви увійшли в систему". В іншому випадку виведіть повідомлення "Неправильний пароль".
#
# 2. **Визначення днів тижня:**
#    Завдання: Створіть програму, яка встановлює номер дня тижня і виводить назву відповідного дня тижня. Якщо номер дня недійсний (менше 1 або більше 7), виведіть повідомлення про помилку.
#
#
# Створіть власні змінні або встановіть початкові значення, щоб виконати ці завдання без використання `input`. Використовуйте умовні конструкції і цикли для розв'язання кожного завдання. Бажаю успіхів у виконанні цих завдань!

# 1. **Перевірка паролю:**
system_password = 'password123'
# input_password = '<PASSWORD>'
input_password = 'password123'
if system_password == input_password:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

# 2. **Визначення днів тижня:**
week_days = {1: 'Понеділок', 2: 'Вівторок', 3: 'Середа', 4: 'Четвер', 5: 'Пʼятниця', 6: 'Субота', 7: 'Неділя'}
# day_number = 1
# day_number = -10
day_number = 88

# if day_number < 1 or day_number > 7:  # Можна ще так
if day_number in week_days.keys():
    print(week_days[day_number])
else:
    print('Помилка: Номер дня', day_number, 'недійсний')

