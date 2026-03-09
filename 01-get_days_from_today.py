#Імпортуємо модуль datetime
from datetime import datetime

#Функція, яка розраховує кількість днів від сьогоднішньої дати до введеної дати
def get_days_from_today(date: str):
    #Блок, якщо код відпрацює
    try:
        #Встановлюємо сьогоднішню дату (без часу)
        today = datetime.today().date()

        #Перетворюємо рядок у об'єкт datetime (без часу)
        date_from_string = datetime.strptime(date, '%Y-%m-%d').date()
        
        #Розраховуємо та повертаємо кількість днів від сьогоднішньої дати до введеної дати
        days_from_today = today - date_from_string

        return days_from_today.days
    #Оброблюємо помилку, якщо введено невірний тип даних
    except TypeError:
        return 'Type error! You have to input a sting'
    
    #Оброблюємо помилку, якщо введено невірний формат дати
    except ValueError:
        return 'Value error! Input valid format: YYYY-MM-DD'