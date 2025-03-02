from functools import reduce
import time
import math

# 1. Умножение всех чисел в списке
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

print(multiply_list([1, 2, 3, 4]))  # 1*2*3*4 = 24


# 2. Подсчет букв верхнего и нижнего регистра
def count_letters(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print(f"Upper case: {upper}, Lower case: {lower}")

count_letters("Hello World")


# 3. Проверка на палиндром
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False


# 4. Квадратный корень после задержки
def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds / 1000)  # Переводим в секунды
    print(f"Square root of {number} after {milliseconds} milliseconds is {math.sqrt(number)}")

delayed_sqrt(25100, 2123)


# 5. Проверка, что все элементы в кортеже True
def all_true(t):
    return all(t)

print(all_true((True, True, True)))  # True
print(all_true((True, False, True)))  # False
