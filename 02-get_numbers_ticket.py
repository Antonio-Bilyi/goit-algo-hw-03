#Імпортуємо модуль random 
import random

#Функція для генерації унікальних випадкових чисел у відповідному діапазоні
def get_numbers_ticket(min: int, max: int, quantity: int):
    #Блок якщо код відпрацює    
    try:
        #Генеруємо список випадкових чисел у відповідному діапазоні
        numbers = range(min, max + 1)

        #Генеруємо список унікальних чисел відповдіної кількості    
        numbers_ticket = random.sample(numbers, quantity)

        #Повертаємо відсортований список унікальних чисел у відповідному діапазоні 
        return sorted(numbers_ticket)
    #Оброблюємо помилку у разі введення невірного типу даних
    except TypeError:
        return 'Error type! You have to input numbers'
    
    #Оброблюємо помилку у разі якщо кількість чисел перевищує діапазон та повертаємо пустий список
    except ValueError:
        print('Sample larger than population')
        return []