#Імпортуємо модуль re
import re

#Функція, яка буде нормалізувати номер телефону користувача
def normalize_phone(phone_number: str) -> str:
    #Блок, якщо код відпрацює
    try:
        #Прибираємо з введеного номеру усє окрім цифр та знака +
        formatted_phone = re.sub(r'[^\d+]', '', phone_number)
        
        #Робимо перевірку якщо відформатований номер починається зі знака +
        if formatted_phone.startswith('+'):
            return formatted_phone
        #Робимо перевірку якщо відформатований номер починається з цифр 380
        elif formatted_phone.startswith('380'):
            return '+' + formatted_phone
        #Виводимо відформатований номер, якщо він не містить міжнародного коду
        else:
            return '+38' + formatted_phone
    #Оброблюємо помилку у разі введення невірного типу номеру телефону
    except TypeError:
        print('Invalid type! Phone number must be a string')
        
    #Оброблюємо помилку у разі введення інших даних окрім номеру телефону
    except ValueError:
        print('Invalid value! You have to input a phone number')