"""
Напишите скрипт, который получает текущее время и дату, а затем выводит их в
формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
недели в году.
"""

from datetime import datetime

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
day_of_week = now.strftime('%A')
week_number = now.isocalendar()[1]

print(f'Current date and time: {formatted_date}')
print(f'Day of the week: {day_of_week}')
print(f'Week number: {week_number}')